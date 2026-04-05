# -*- coding: utf-8 -*-
"""Generate one digest markdown per chapter (04-07, 13-40) from 正文 v1."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1].parent
OUT = ROOT / "素材库" / "颗粒摘录"
V1_GLOB = "《蚀名簿》正文_第*_v1.md"

# Chapters already covered by fine-grained 20260406_* files
SKIP = {8, 9, 10, 11, 12}

HEAD_RE = re.compile(r"^# 第\s*(\d+)\s*节[：:]\s*(.+?)\s*（")


def parse_head(lines: list[str]) -> tuple[int, str]:
    for line in lines[:5]:
        m = HEAD_RE.match(line.strip())
        if m:
            return int(m.group(1)), m.group(2).strip()
    raise ValueError("no heading: " + lines[0][:80])


def chunk_lines(lines: list[str], max_chunks: int = 3, max_excerpt: int = 42) -> list[tuple[int, int, list[str]]]:
    """Return list of (start_1based, end_1based, excerpt_lines). Split on ---; shrink to <=3 chunks."""
    parts: list[tuple[int, list[str]]] = []
    current: list[str] = []
    start = 1
    for line in lines:
        if line.strip() == "---" and current:
            parts.append((start, current))
            start += len(current) + 1
            current = []
        else:
            current.append(line)
    if current:
        parts.append((start, current))

    if not parts:
        parts = [(1, lines)]

    def split_thirds(st: int, seg: list[str], n: int = 3) -> list[tuple[int, list[str]]]:
        L = len(seg)
        if L < 60:
            return [(st, seg)]
        cuts = [0]
        for k in range(1, n):
            cuts.append((L * k) // n)
        cuts.append(L)
        out_t: list[tuple[int, list[str]]] = []
        off = st
        for a, b in zip(cuts, cuts[1:]):
            chunk = seg[a:b]
            out_t.append((off, chunk))
            off += len(chunk)
        return out_t

    # 无 --- 或仅一块过长：按行切成至多 3 块
    if len(parts) == 1 and len(parts[0][1]) > 120:
        st0, seg0 = parts[0]
        parts = split_thirds(st0, seg0, max_chunks)

    def merge_to_n(segs: list[tuple[int, list[str]]], n: int) -> list[tuple[int, list[str]]]:
        if len(segs) <= n:
            return segs
        # bucket consecutive segments into n groups by line count
        total = sum(len(t[1]) for t in segs)
        target = total / n
        out_b: list[tuple[int, list[str]]] = []
        acc: list[str] = []
        acc_start = segs[0][0]
        acc_len = 0
        bucket = 1
        for st, seg in segs:
            if not acc:
                acc_start = st
            acc.extend(seg)
            acc_len += len(seg)
            if bucket < n and acc_len >= target * 0.85:
                out_b.append((acc_start, acc))
                acc = []
                acc_len = 0
                bucket += 1
        if acc:
            out_b.append((acc_start, acc))
        # fix: if last bucket empty, merge
        while len(out_b) > n:
            a, b = out_b[-2], out_b[-1]
            out_b[-2] = (a[0], a[1] + b[1])
            out_b.pop()
        return out_b[:n]

    parts = merge_to_n(parts, max_chunks)

    out: list[tuple[int, int, list[str]]] = []
    for st, seg in parts[:max_chunks]:
        ex = seg[:max_excerpt]
        end_ex = st + len(ex) - 1
        out.append((st, end_ex, ex))
    return out


def role_for_index(idx: int, n: int) -> str:
    if idx == 0:
        return "开场气氛与钩子"
    if idx == n - 1:
        return "收束或转折"
    return "中段推进"


def main() -> None:
    files = sorted(ROOT.glob(V1_GLOB), key=lambda p: p.name)
    rows_index: list[str] = []
    rows_compare: list[str] = []

    for fp in files:
        text = fp.read_text(encoding="utf-8")
        lines = text.splitlines()
        num, title = parse_head(lines)
        if num in SKIP:
            continue

        rel = f"../../{fp.name}"
        chunks = chunk_lines(lines)
        digest_name = f"20260411_{num:02d}_{title}_摘编.md"
        out_path = OUT / digest_name

        parts_md: list[str] = []
        parts_md.append(f"# 摘编：第 {num:02d} 节《{title}》（母本 v1）\n\n")
        parts_md.append(f"- **母本**：[`{rel}`]({rel})\n")
        parts_md.append(
            "- **整理说明**：本文件为**一节一摘编**（优先按母本 `---` 分块并合并为至多 3 段；无分块则按行三等分）。每段取前若干行摘录；细拆见同节 `20260406_*`；写新稿务必回母本核对因果。\n"
        )
        parts_md.append("- **冲突提醒**：与《真设定集V4》《长篇骨架》对表后再定嵌用；旧稿视角/动线与新结构不一致处，以新骨架为准改写。\n")

        for i, (st, en, ex) in enumerate(chunks):
            role = role_for_index(i, len(chunks))
            parts_md.append(f"\n---\n\n## 颗粒 {i + 1}（节选 L{st}–L{en}）·{role}\n\n")
            parts_md.append("```\n")
            parts_md.extend(l + "\n" for l in ex)
            parts_md.append("```\n")

        out_path.write_text("".join(parts_md), encoding="utf-8")

        rows_index.append(
            f"| `{digest_name}` | [`{rel}`]({rel}) | 侵/啮/穴·第{num:02d}节整节素材 | 摘编体；回母本核对 |"
        )
        rows_compare.append(
            f"| {num:02d}《{title}》v1 | 见摘编内分块与摘录 | 新结构待定 | 按骨架重挂功能句 | 待定 | `{digest_name}` |"
        )

    print("Wrote", len(rows_index), "digest files")
    (OUT / "_generated_index_rows.md").write_text("\n".join(rows_index) + "\n", encoding="utf-8")
    (OUT / "_generated_compare_rows.md").write_text("\n".join(rows_compare) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
