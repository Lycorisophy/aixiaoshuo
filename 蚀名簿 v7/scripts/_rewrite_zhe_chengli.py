# -*- coding: utf-8 -*-
"""Rewrite repetitive 在这城里，常常是 in B-line prose; keep first N per #正文 block."""
import re
from pathlib import Path

KEEP = 10
MARKER = "在这城里，常常是"


def alternate(seg: str, k: int) -> str:
    """seg is text AFTER marker (first char may be ** or Chinese)."""
    alts = [
        lambda s: "多半" + s,
        lambda s: "不过是" + s,
        lambda s: "说穿了，" + s,
        lambda s: s + "——城里多这样",
        lambda s: "无非是" + s if s.startswith("**") else "就" + s,
        lambda s: "横竖" + s if len(s) < 18 else "总之" + s,
        lambda s: "左右" + s if s.startswith("**") else "说到底，" + s,
        lambda s: "到头来，" + s,
    ]
    return alts[k % len(alts)](seg)


def process_block(rest: str) -> str:
    if MARKER not in rest:
        return rest
    parts = rest.split(MARKER)
    out = [parts[0]]
    occ = 0
    for seg in parts[1:]:
        occ += 1
        if occ <= KEEP:
            out.append(MARKER + seg)
        else:
            out.append(alternate(seg, occ - KEEP - 1))
    return "".join(out)


def process_file(path: Path) -> tuple[int, int]:
    t = path.read_text(encoding="utf-8")
    if "# 正文" not in t:
        return 0, 0
    head, body = t.split("# 正文", 1)
    before = body.count(MARKER)
    new_body = process_block(body)
    after = new_body.count(MARKER)
    path.write_text(head + "# 正文" + new_body, encoding="utf-8")
    return before, after


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent / "正文分节"
    for name in [
        "《蚀名簿》第2幕第2节.md",
        "《蚀名簿》第2幕第3节.md",
        "《蚀名簿》第2幕第4节.md",
        "《蚀名簿》第2幕第5节.md",
        "《蚀名簿》第2幕第6节.md",
    ]:
        p = root / name
        b, a = process_file(p)
        print(p.name, "marker", b, "->", a)
