# -*- coding: utf-8 -*-
"""
从 v1 源重新生成「连载润色版」分节文件：**只做版式与合并，不做池文扩写**。

- 合并 v1 一句一空行 → 完整段落
- 去掉 # / ## 标题行；文首统一一行「蚀名簿·第X章（幕）·第XX节　篇名」
- 去 **、弯引号→「」、1986 错代（快递分拣）
- 段首「　　」

若需 **≥5000 字**，应在本节情节缝内人工/Agent 加：场景过渡、动作细部、节制修饰、偶尔心理，
勿再使用 expand_lianzai_to_5000 / expand_lianzai_tiered 的模板池垫尾。
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent
INTRO = ROOT / "《蚀名簿》正文_序+01-03节_v1.md"

_spec_em = importlib.util.spec_from_file_location("em", OUT / "expand_lianzai_to_5000.py")
_em = importlib.util.module_from_spec(_spec_em)
assert _spec_em and _spec_em.loader
_spec_em.loader.exec_module(_em)

_spec_cv = importlib.util.spec_from_file_location("cv", OUT / "copy_v1_rename.py")
_cv = importlib.util.module_from_spec(_spec_cv)
assert _spec_cv and _spec_cv.loader
_spec_cv.loader.exec_module(_cv)

split_intro = _cv.split_intro
find_v1 = _cv.find_v1
outfile_name = _cv.outfile_name
SECTION_META = _cv.SECTION_META
cn_section_num = _cv.cn_section_num


def strip_hash_lines(text: str) -> str:
    """去掉所有 Markdown 标题行（# 开头），保留计划中的单独文首行由本脚本写入。"""
    return "\n".join(
        ln for ln in text.splitlines() if not ln.strip().startswith("#")
    )


def process_raw(md: str, section: int) -> str:
    merged = _em.merge_staccato_blocks(md)
    merged = _em.strip_h2_headers(merged)
    merged = strip_hash_lines(merged)
    merged = _em.normalize_markdown(merged)
    body = merged.strip()
    body_book = _em.bookify_body(body)
    ch, mumu, title = SECTION_META[section - 1]
    sn = cn_section_num(section)
    head = f"蚀名簿·第{ch}章（{mumu}）·第{sn}节　{title}"
    return head + "\n\n" + body_book.rstrip() + "\n"


def main() -> None:
    if not INTRO.exists():
        raise FileNotFoundError(INTRO)
    intro_text = INTRO.read_text(encoding="utf-8")
    s01, s02, s03 = split_intro(intro_text)

    for sec in range(1, 41):
        if sec == 1:
            raw = s01
        elif sec == 2:
            raw = s02
        elif sec == 3:
            raw = s03
        else:
            raw = find_v1(sec).read_text(encoding="utf-8")
        text = process_raw(raw, sec)
        dest = OUT / outfile_name(sec)
        dest.write_text(text, encoding="utf-8")
        print(f"{sec:02d} -> {dest.name} len={len(text)}")

    print("完成：无池文；字数因节而异。合并全书请运行 merge_lianzai_to_one.py")


if __name__ == "__main__":
    main()
