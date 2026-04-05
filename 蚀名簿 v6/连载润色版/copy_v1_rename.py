# -*- coding: utf-8 -*-
"""将 v1 正文按节拷贝到连载润色版：1–3 从序+01-03 拆分，4–40 从独立 v1 文件复制；仅重命名，不改正文。"""
from __future__ import annotations

import glob
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
INTRO = ROOT / "《蚀名簿》正文_序+01-03节_v1.md"

# 节号 1..40 -> (章中文, 幕名, 篇名)
SECTION_META: list[tuple[str, str, str]] = [
    ("一", "侵", "序与雨落铅灰"),
    ("一", "侵", "纸铺遗音"),
    ("一", "侵", "古井幽幽"),
    ("一", "侵", "名册初现"),
    ("一", "侵", "雾中逢君"),
    ("一", "侵", "纸翁缄默"),
    ("一", "侵", "户籍涂痕"),
    ("一", "侵", "决意下井"),
    ("二", "啮", "暗流涌动"),
    ("二", "啮", "雨夜来客"),
    ("二", "啮", "晨昏抉择"),
    ("二", "啮", "黄昏之前"),
    ("二", "啮", "夜行如谜"),
    ("二", "啮", "档案迷宫"),
    ("二", "啮", "雨夜迷途"),
    ("二", "啮", "无名归途"),
    ("三", "穴", "待归之人"),
    ("三", "穴", "档案残页"),
    ("三", "穴", "涂改之痕"),
    ("三", "穴", "空白之页"),
    ("三", "穴", "日记残章"),
    ("三", "穴", "暗格寻踪"),
    ("三", "穴", "对质之困"),
    ("三", "穴", "无名之径"),
    ("四", "耗", "雨歇之处"),
    ("四", "耗", "旧居之门"),
    ("四", "耗", "井底非井"),
    ("四", "耗", "无底之井"),
    ("四", "耗", "井底之声"),
    ("四", "耗", "归位之人"),
    ("四", "耗", "双生之影"),
    ("四", "耗", "记忆残片"),
    ("五", "朽", "证据成链"),
    ("五", "朽", "舆论如潮"),
    ("五", "朽", "言临留书"),
    ("五", "朽", "晚照之问"),
    ("五", "朽", "纸翁作证"),
    ("五", "朽", "记忆归处"),
    ("五", "朽", "档案馆中"),
    ("五", "朽", "雨落如初"),
]


def cn_section_num(n: int) -> str:
    digits = "零一二三四五六七八九"
    if n <= 10:
        return digits[n] if n != 10 else "十"
    if n < 20:
        return "十" + (digits[n % 10] if n != 10 else "")
    if n < 100:
        t, o = divmod(n, 10)
        if t == 1:
            return "十" + (digits[o] if o else "")
        if o == 0:
            return digits[t] + "十"
        return digits[t] + "十" + digits[o]
    raise ValueError(n)


def outfile_name(section: int) -> str:
    ch, mumu, title = SECTION_META[section - 1]
    sn = cn_section_num(section)
    return f"蚀名簿第{ch}章{mumu}第{sn}节{title}.md"


def split_intro(text: str) -> tuple[str, str, str]:
    m2 = re.search(r"^## 第 02 节", text, re.M)
    m3 = re.search(r"^## 第 03 节", text, re.M)
    if not m2 or not m3:
        raise RuntimeError("《蚀名簿》正文_序+01-03节_v1.md 缺少 ## 第 02/03 节 锚点")
    # 第一节：卷头至第 02 节标题前（含 # 全书标题、序、第 01 节）
    s01 = text[: m2.start()].strip() + "\n"
    s02 = text[m2.start() : m3.start()].strip() + "\n"
    s03 = text[m3.start() :].strip() + "\n"
    return s01, s02, s03


def find_v1(section: int) -> Path:
    pat = str(ROOT / f"《蚀名簿》正文_第{section:02d}节*_v1.md")
    hits = sorted(p for p in glob.glob(pat) if "样稿" not in p and str(p).endswith("_v1.md"))
    if not hits:
        raise FileNotFoundError(pat)
    return Path(hits[0])


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    intro_text = INTRO.read_text(encoding="utf-8")
    s01, s02, s03 = split_intro(intro_text)

    for sec in range(1, 41):
        name = outfile_name(sec)
        dest = OUT / name
        if sec == 1:
            body = s01
        elif sec == 2:
            body = s02
        elif sec == 3:
            body = s03
        else:
            src = find_v1(sec)
            body = src.read_text(encoding="utf-8")
            if not body.endswith("\n"):
                body += "\n"
        dest.write_text(body, encoding="utf-8")
        print(f"{sec:02d} -> {name}")

    print(f"完成：共 40 个文件 -> {OUT}")


if __name__ == "__main__":
    main()
