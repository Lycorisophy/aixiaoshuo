# -*- coding: utf-8 -*-
"""Batch inventory + sanitize #正文 for 第3～5幕分节."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SECTION = ROOT / "正文分节"
MARKER = "# 正文"


def cjk_count(s: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", s))


def extract_yaml_05(text: str) -> str:
    m = re.search(r"对应_05_事件序号:\s*\[(.*?)\]", text, re.S)
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1).strip())


def split_at_body(text: str) -> tuple[str, str] | tuple[None, None]:
    idx = text.find(MARKER)
    if idx < 0:
        return None, None
    head = text[: idx + len(MARKER)]
    body = text[idx + len(MARKER) :]
    body = body.lstrip("\n\r")
    return head, body


def sanitize_body(body: str) -> str:
    body = re.sub(r"\*\*([^*]+)\*\*", r"\1", body)
    # 不成对的 **（常见于节末导航句被半剥后）
    body = body.replace("**", "")
    lines = []
    for line in body.splitlines():
        if line.strip() == "---":
            lines.append("")
        else:
            lines.append(line)
    out = "\n".join(lines)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.rstrip() + "\n"


def update_remark_cjk(head: str, body_cjk: int) -> str:
    """Update **#正文** CJK **约 N** or **#正文**起 CJK **约 N** in 备注 line."""

    def repl(m: re.Match) -> str:
        return m.group(1) + str(body_cjk) + m.group(3)

    # **#正文**起 CJK **约 1234** or **#正文** CJK **约 1234**
    pat1 = r"(\*\*#正文\*\*(?:起)?\s*CJK\s*\*\*约\s*)\d+(\*\*)"
    if re.search(pat1, head):
        return re.sub(pat1, lambda m: m.group(1) + str(body_cjk) + m.group(2), head, count=1)

    # 第4幕第1节: **#正文** **5004**
    pat2 = r"(\*\*#正文\*\*\s*\*\*)(\d+)(\*\*)"
    if re.search(pat2, head):
        return re.sub(pat2, lambda m: m.group(1) + str(body_cjk) + m.group(3), head, count=1)

    # 5幕8: **#正文**含尾声 CJK **约 2800**
    pat4 = r"(\*\*#正文\*\*含尾声 CJK\s*\*\*约\s*)\d+(\*\*)"
    if re.search(pat4, head):
        return re.sub(pat4, lambda m: m.group(1) + str(body_cjk) + m.group(2), head, count=1)

    return head


def process_file(path: Path, dry_run: bool = False) -> dict:
    text = path.read_text(encoding="utf-8")
    head, body = split_at_body(text)
    if head is None:
        return {"file": path.name, "error": "no # 正文"}
    orig_body = body
    new_body = sanitize_body(body)
    body_cjk = cjk_count(new_body)
    new_head = update_remark_cjk(head, body_cjk)
    out = new_head + "\n\n" + new_body
    if not dry_run:
        path.write_text(out, encoding="utf-8")
    return {
        "file": path.name,
        "cjk": body_cjk,
        "dash_lines": orig_body.count("\n---\n") + (1 if orig_body.strip() == "---" else 0),
        "stars": len(re.findall(r"\*\*[^*]+\*\*", orig_body)),
    }


def list_act35_files() -> list[Path]:
    out = []
    for act in (3, 4, 5):
        max_sec = 16 if act == 4 else 8
        for sec in range(1, max_sec + 1):
            p = SECTION / f"《蚀名簿》第{act}幕第{sec}节.md"
            if p.exists():
                out.append(p)
    return out


def inventory() -> str:
    rows = []
    rows.append("# 第3～5幕 体例篇幅审计（工具生成）\n")
    rows.append("\n| 文件 | 05序号 | #正文CJK | 正文内`---`块(估) | 正文内`**`对(估) |\n")
    rows.append("|------|--------|----------|-------------------|----------------|\n")
    seq_groups: dict[str, list[tuple[str, int]]] = {}
    for path in list_act35_files():
        text = path.read_text(encoding="utf-8")
        head, body = split_at_body(text)
        if body is None:
            continue
        y05 = extract_yaml_05(text)
        cjk = cjk_count(body)
        dashes = body.count("\n---\n") + body.count("\n---\r\n")
        if body.strip() == "---":
            dashes += 1
        stars = len(re.findall(r"\*\*[^*]+\*\*", body))
        key = re.sub(r'["\s]', "", y05.split(",")[0]) if y05 else ""
        seq_groups.setdefault(key, []).append((path.name, cjk))
        rows.append(f"| {path.name} | {y05[:40]}… | {cjk} | {dashes} | {stars} |\n")

    rows.append("\n## 同05序号 正文CJK小计（供044/046/047/048等）\n\n")
    for k, items in sorted(seq_groups.items()):
        if not k:
            continue
        s = sum(x[1] for x in items)
        if len(items) > 1 or k.startswith("044") or k.startswith("046"):
            rows.append(f"- **{k}**（{len(items)}文件）: 合计约 **{s}** CJK — " + ", ".join(f"{n}:{c}" for n, c in items) + "\n")

    return "".join(rows)


def main():
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--inventory-only", action="store_true")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    inv_path = ROOT / "自检_第3～5幕_体例篇幅审计.md"
    inv_path.write_text(inventory(), encoding="utf-8")
    print("Wrote", inv_path)

    if args.apply:
        for p in list_act35_files():
            process_file(p, dry_run=False)
            print("OK", p.name)


if __name__ == "__main__":
    main()
