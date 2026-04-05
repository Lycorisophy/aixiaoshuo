# -*- coding: utf-8 -*-
"""按第 01–40 节顺序合并连载润色版分节文件为单一蚀名簿.md。"""
from __future__ import annotations

import importlib.util
from pathlib import Path

OUT = Path(__file__).resolve().parent
DEST = OUT / "蚀名簿.md"

_spec = importlib.util.spec_from_file_location("cv", OUT / "copy_v1_rename.py")
_cv = importlib.util.module_from_spec(_spec)
assert _spec and _spec.loader
_spec.loader.exec_module(_cv)
outfile_name = _cv.outfile_name
SECTION_META = _cv.SECTION_META
cn_section_num = _cv.cn_section_num


def main() -> None:
    blocks: list[str] = []
    missing: list[str] = []

    header = "# 蚀名簿\n\n> 连载润色版合并稿 · 全四十节 · UTF-8"
    blocks.append(header)

    for sec in range(1, 41):
        name = outfile_name(sec)
        path = OUT / name
        if not path.exists():
            missing.append(name)
            continue
        ch, mumu, title = SECTION_META[sec - 1]
        sn = cn_section_num(sec)
        divider = (
            f"\n\n---\n\n"
            f"蚀名簿·第{ch}章（{mumu}）·第{sn}节　{title}\n\n"
            f"---\n\n"
        )
        body = path.read_text(encoding="utf-8").strip()
        blocks.append(divider + body)

    if missing:
        raise SystemExit(f"缺失分节文件（共 {len(missing)} 个）：\n" + "\n".join(missing))

    merged = "\n".join(blocks) + "\n"
    DEST.write_text(merged, encoding="utf-8")
    print(f"已写入 {DEST} ，字符数 len = {len(merged)}")


if __name__ == "__main__":
    main()
