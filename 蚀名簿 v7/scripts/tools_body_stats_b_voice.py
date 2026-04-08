# -*- coding: utf-8 -*-
"""只读统计：# 正文 之后的「在这城里」等密度与极短独行段占比。"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

MARKER = "# 正文"
PAT_ZLC = re.compile("在这城里")
PAT_ZLC_OFTEN = re.compile("在这城里，常常是")
PAT_ZLC_SHI = re.compile("在这时候")


def body_after(path: Path) -> str:
    t = path.read_text(encoding="utf-8")
    i = t.find(MARKER)
    if i < 0:
        return ""
    return t[i + len(MARKER) :].lstrip("\n\r")


def stats(body: str) -> dict:
    paras = re.split(r"\n\s*\n", body.strip())
    short_para = 0
    for p in paras:
        lines = [ln.strip() for ln in p.splitlines() if ln.strip()]
        if len(lines) == 1 and len(lines[0]) < 15:
            short_para += 1
    return {
        "zai_zhe_li": len(PAT_ZLC.findall(body)),
        "zai_zhe_li_changchang": len(PAT_ZLC_OFTEN.findall(body)),
        "zai_zhe_shihou": len(PAT_ZLC_SHI.findall(body)),
        "paras": len(paras),
        "short_single_line_paras": short_para,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+", type=Path, help="md files")
    args = ap.parse_args()
    for p in args.paths:
        b = body_after(p)
        if not b:
            print(p.name, "(no # 正文)")
            continue
        s = stats(b)
        print(
            f"{p.name}\t在这城里={s['zai_zhe_li']}\t在这城里常常是={s['zai_zhe_li_changchang']}\t在这时候={s['zai_zhe_shihou']}\t段数={s['paras']}\t极短独行段(<15字)={s['short_single_line_paras']}"
        )


if __name__ == "__main__":
    main()
