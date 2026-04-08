# -*- coding: utf-8 -*-
"""
将第4幕 B 视角正文中相邻的「链式短段」合并为一句/少句，降低模板频率。
仅处理 # 正文 之后；不碰 YAML。规则保守：只合并结构明确的接续关系。
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

MARKER = "# 正文"

P_OFTEN = re.compile(r"^(.+?)在这城里，常常是(.+?)。$")
P_NOT_OFTEN = re.compile(r"^(.+?)在这城里，常常不是(.+?)。$")
P_NOT_SIMPLE = re.compile(r"^(.+?)在这城里，不是(.+?)。$")
P_SHI = re.compile(r"^(.+?)在这时候，是(.+?)。$")
P_NOT = re.compile(r"^(.+?)在这时候，不是(.+?)。$")
P_NEQ = re.compile(r"^(.+?)在这时候，不等于(.+?)。$")
P_IS = re.compile(r"^是(.+?)。$")


def chain_ok(mid: str, subj: str) -> bool:
    mid, subj = mid.strip(), subj.strip()
    if not mid or not subj:
        return False
    if subj == mid or mid.endswith(subj):
        return True
    if mid[-1] == subj[0]:
        return True
    if 1 < len(subj) <= 6 and subj in mid:
        return True
    return False


def merge_once(lines: list[str]) -> tuple[list[str], bool]:
    out: list[str] = []
    i = 0
    changed = False
    while i < len(lines):
        a = lines[i]

        # 常常是 + 在这时候不是 + 是xxx。
        if i + 2 < len(lines):
            m1 = P_OFTEN.match(a)
            m2 = P_NOT.match(lines[i + 1])
            m3 = P_IS.match(lines[i + 2])
            if m1 and m2 and m3 and chain_ok(m1.group(2), m2.group(1)):
                merged = (
                    f"{m1.group(1)}在这城里，常常是{m1.group(2)}；"
                    f"{m2.group(1)}在这时候，不是{m2.group(2)}，而是{m3.group(1)}。"
                )
                out.append(merged)
                i += 3
                changed = True
                continue

        # 常常是 + 在这时候是
        if i + 1 < len(lines):
            m1 = P_OFTEN.match(a)
            m2 = P_SHI.match(lines[i + 1])
            if m1 and m2 and chain_ok(m1.group(2), m2.group(1)):
                merged = f"{m1.group(1)}在这城里，常常是{m1.group(2)}；{m2.group(1)}在这时候，是{m2.group(2)}。"
                out.append(merged)
                i += 2
                changed = True
                continue

        # 常常是 + 在这时候不等于
        if i + 1 < len(lines):
            m1 = P_OFTEN.match(a)
            m2 = P_NEQ.match(lines[i + 1])
            if m1 and m2 and chain_ok(m1.group(2), m2.group(1)):
                merged = f"{m1.group(1)}在这城里，常常是{m1.group(2)}；{m2.group(1)}在这时候，不等于{m2.group(2)}。"
                out.append(merged)
                i += 2
                changed = True
                continue

        # 在这城里，不是 + 是xxx。
        if i + 1 < len(lines):
            m1 = P_NOT_SIMPLE.match(a)
            m2 = P_IS.match(lines[i + 1])
            if m1 and m2:
                merged = f"{m1.group(1)}在这城里，不是{m1.group(2)}，而是{m2.group(1)}。"
                out.append(merged)
                i += 2
                changed = True
                continue

        # 常常不是 + 是xxx。
        if i + 1 < len(lines):
            m1 = P_NOT_OFTEN.match(a)
            m2 = P_IS.match(lines[i + 1])
            if m1 and m2:
                merged = f"{m1.group(1)}在这城里，常常不是{m1.group(2)}，而是{m2.group(1)}。"
                out.append(merged)
                i += 2
                changed = True
                continue

        out.append(a)
        i += 1
    return out, changed


def flatten_paragraphs(body: str) -> list[str]:
    paras = [p.strip() for p in re.split(r"\n\s*\n", body.strip()) if p.strip()]
    flat: list[str] = []
    for p in paras:
        for ln in p.splitlines():
            s = ln.strip()
            if s:
                flat.append(s)
    return flat


def merge_all_passes(flat: list[str]) -> list[str]:
    cur = flat
    for _ in range(500):
        nxt, ch = merge_once(cur)
        cur = nxt
        if not ch:
            break
    return cur


def rebuild_body(body: str, merged_lines: list[str]) -> str:
    tail = body[len(body.rstrip()) :] if body.endswith("\n") else ""
    core = "\n\n".join(merged_lines)
    if body.strip() and not core.endswith("\n"):
        core += "\n"
    return core + (tail if tail else "")


def process_file(path: Path, dry: bool) -> dict:
    text = path.read_text(encoding="utf-8")
    idx = text.find(MARKER)
    if idx < 0:
        return {"error": "no marker"}
    head = text[: idx + len(MARKER)]
    body = text[idx + len(MARKER) :]
    if body.startswith("\n"):
        body_rest = body[1:]
    else:
        body_rest = body

    flat = flatten_paragraphs(body_rest)
    merged = merge_all_passes(flat)
    new_body = "\n" + rebuild_body(body_rest.lstrip("\n\r"), merged)
    new_text = head + new_body

    if not dry:
        path.write_text(new_text, encoding="utf-8")
    return {
        "flat_lines": len(flat),
        "merged_lines": len(merged),
        "saved": not dry,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    for p in args.paths:
        r = process_file(p, dry=args.dry_run)
        print(p.name, r)


if __name__ == "__main__":
    main()
