# -*- coding: utf-8 -*-
"""
分层扩写：按节目标字数用 EXT 池在节中/文末垫字。

【重要】与 expand_lianzai_to_5000 同属「模板池」路线，**易显废话感**；仅作字数保底实验。
终稿扩写请以情节内场景/动作/修饰/心理为主；净版式请用 lianzai_polish_merge_only.py。
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

OUT = Path(__file__).resolve().parent

_spec = importlib.util.spec_from_file_location("cv", OUT / "copy_v1_rename.py")
_cv = importlib.util.module_from_spec(_spec)
assert _spec and _spec.loader
_spec.loader.exec_module(_cv)
outfile_name = _cv.outfile_name

# 与 _section_targets.md 同步
HEAVY_SECTIONS: frozenset[int] = frozenset(
    {4, 8, 9, 12, 14, 15, 16, 22, 23, 27, 28, 29, 33, 34, 35, 37, 39, 40}
)
REGULAR_MIN, REGULAR_MAX = 6000, 7500
HEAVY_MIN, HEAVY_MAX = 8000, 10000
ABS_MAX = 12000
SECTION_18_SKIP_IF_GE = 6000  # 已达常规带则不再加（计划：偏长节维持）


def is_b_section(sec: int) -> bool:
    return 9 <= sec <= 16 or 25 <= sec <= 32


def target_min(sec: int) -> int:
    if sec in HEAVY_SECTIONS:
        return HEAVY_MIN
    return REGULAR_MIN


def should_skip_section(sec: int, current_len: int) -> bool:
    if sec == 18 and current_len >= SECTION_18_SKIP_IF_GE:
        return True
    if current_len >= target_min(sec):
        return True
    return False


# ---------- 二阶扩充池（与 expand_lianzai_to_5000 池文不重复，01–32 无 E 字样）----------
EXT_A = [
    "风从领口灌进去时，我会下意识摸一下口袋里的纸片。纸片若受潮发软，边缘就会卷，卷得像想逃。逃的不是纸，是人想把责任推给物的本能。我提醒自己：物证只会躺在那里，会动的是手与权限。",
    "巷口的公用电话亭玻璃裂了一道，裂纹把外面的灯割成两半。我投币，听筒贴在耳上，金属味和汗味混在一起，像某种廉价的誓言。誓言若太便宜，往往只够买一句「回头再说」——而「回头」在档案里常常等于「永不」。",
    "旧木窗棂被雨泡胀，胀到推合时发出黏腻的摩擦声。那声音让人想起糨糊：能把东西粘住，也能把东西封死。封死之后，外面的人只能看见一个轮廓，轮廓里发生的一切都成了「室内事务」。",
    "我把鞋底的泥刮在阶沿上，泥落下时带一点腥。腥来自工地还是来自河滩，其实分不清；分不清时，人就会用更大的词去填——比如命运，比如劫数。可我更信小词：泥、印、登记、复印件。",
    "茶缸沿有一圈茶垢，茶垢厚的地方颜色深，像有人反复在同一个位置停嘴。停嘴处往往也是停话处：话到嘴边，被热气一熏，就缩回去。缩回去的话不会消失，只会沉到胃里去发酵。",
    "走廊灯泡外罩着铁丝网，网眼把光切成小方块。站在下面，人会觉得自己也被切成小方块，方便被贴标签、归档、塞进抽屉。抽屉一关，世界就安静——安静得不像解决问题，像解决提问的人。",
    "我指节敲桌面三下，停一下，再敲一下。敲不是为了提醒别人，是为了提醒我自己：别急着把因果写圆。因果一圆，读者舒服，现实却常常故意留一个尖角，尖角专门用来划手。",
    "纸角卷起时，我会用指甲把它压平。压平的动作很徒劳，潮气一来它还会卷。可徒劳也有意义：它让你记住「表面服从」并不等于「内部同意」。档案服从装订，人不一定要服从档案。",
    "雨夜里，远处狗叫两声就停。停得太快，像被人捂嘴。我喜欢把这种停写进笔记——不是当结论，当提醒：城里很多声音不是自然结束，是被掐断。掐断处往往靠近权力，也靠近钱。",
    "玻璃柜台下面的影子比上面深。深的影子适合藏手：手在阴影里数钱、递条、交换复印件，都像在演戏。演戏若演久了，演员会忘了哪一段是台词，哪一段是生活。",
    "我闻见消毒水味，就知道离「正式场合」近了。正式场合的特点是：你越疼，越要站直；你越想问，越要先填表。表一填，问题就被翻译成「流程」，流程最擅长把尖锐磨钝。",
    "铅笔印浅，浅得像不想承担责任。可浅印反复擦写，纸纤维会起毛，起毛后反而更难否认「有人在这里犹豫过」。犹豫的痕迹，有时比签字更说明问题。",
    "门帘掀起时，风会先把里面的气味送出来：霉、铁、还有一点甜。甜若出现在不该甜的地方，就会像笑出现在葬礼上——不是不合时宜，是让人警觉：这里有人刻意调和过什么。",
    "我把手表摘下来，表带内侧潮得发白。发白像皮肤在抗议：你别再用「几点了」去压我。时间在这件事里确实重要，但更重要的是：谁掌握记录时间的笔。",
    "台阶边的苔藓厚，厚得像一层不肯说话的绿。踩上去滑，滑一下，人会突然谦逊——谦逊不是因为懂礼貌，是因为怕摔。怕摔的人，往往更注意脚下有没有被人动过。",
    "窗纸上有雨点洇开的斑，斑边毛毛的，像旧照片受潮。旧照片和旧档案是同一种东西：都在提醒你，「过去」不是消失了，是换了一种更软的形态贴在你眼前。",
    "我握紧伞骨，骨节发出轻微的一响。那响很小，小得像提醒：支撑你的东西也会疲劳。疲劳到一定程度，就会在某个风雨夜突然翻过去——翻过去时，往往最先湿的是脸。",
    "铁皮信箱口锈成褐色，褐得像陈年血印。投进去的信不是消失，是进入另一条队列：排队、被分拣、被贴上「可查/不可查」。可查与不可查之间，站着的从来不是邮差，是权限。",
    "屋里钟表走声很干，干得像在数颗粒。颗粒数多了，人就会错觉自己也被数进去。被数的感觉不坏，坏的是：你不知道自己被归在哪一格。",
    "我离开前回头看一眼桌面。桌面空不空不重要，重要的是：有没有留下「刚被人抹过」的秩序。秩序太干净，像有人用抹布把指纹连同问题一起擦掉。",
]

EXT_B = [
    "我把呼吸放慢，慢到能数清绳子的纹理。纹理里嵌着旧潮，旧潮里有别人的手温。手温这种东西最麻烦：它会让你误以为自己「接过」了什么，其实你只是被接过。",
    "上面传来的声音经过井筒变扁，扁得像纸条。纸条递下来时不必写字，空白就够。空白在下面是压力，在上面是策略——我懂，所以我尽量不抬头接。",
    "井壁某一截特别滑，滑得像有人常摸。常摸的地方不会无缘无故：要么为了借力，要么为了确认「还在」。确认这种事，做多了会像上瘾，上瘾会像认罪。",
    "我把手套指节处抻平，抻平也会留下褶。褶像记录：你刚才抓过什么、松过什么。松比抓更难看，因为松的时候，东西往往已经不在你手里了。",
    "光斑在脚边游，游得像鱼。鱼不咬钩也危险：它让你分神。分神在这里不是小事，是分一寸就少一寸生路。我把目光钉在暗处，暗处至少诚实——诚实到不发誓。",
    "潮气里有一股很淡的甜味，甜得像腐烂前的回光。回光一现，人就会错觉「还来得及」。来得及这句话，在井里最贵，也最容易骗人。",
    "我听见自己的心跳，跳得像越界。越界的心跳我不责备：它提醒我还活着。活着的人会怕，怕的人会想抓点什么；我抓绳，绳抓我，我们互相作证。",
    "上面有人咳嗽，咳嗽声被井筒切成三截。三截落下时次序乱了，像有人在故意打乱节奏。节奏一乱，你就会怀疑：那是人咳，还是风在学着咳。",
    "我把舌尖抵住上颚，抵住是为了不把字吐出去。字吐出去会落地，落地会生根。根若生在井里，就会往上长，长到某一天把你也缠进去。",
    "绳影晃一下，晃得像试探。试探不是温柔，是计算：你怕不怕，你会不会退。退在岸上是理智，在井里像把最后一点骨气也交了。",
    "我数脚步，脚步轻得不象人。轻得像纸。纸在潮里会软，软了还能写字；人软了，就只能跟着别人的笔画走。我不让自己软，我让自己疼。疼至少方向明确。",
    "井底的静不是无声，是声被吞了。吞声的东西如果有形状，大概像一张湿棉被：捂住你，还让你觉得自己安全。安全这种感觉，在这里最可疑。",
    "我把目光从水面移开。水面会记账：你看了它多久，它就还你多久幻觉。幻觉我不需要，我需要的是能用手摸到的粗糙——粗糙不漂亮，但不撒谎。",
    "上面滴下一滴水，水滴在肩上，冷得像提醒。提醒不必大声：大声属于岸上。岸上的大声到了下面，只会变成更细的针，专门扎那些还想解释的人。",
    "我收紧下颌，收紧是为了不让喉咙自己开门。喉咙一开门，名字就会排队往外跑。名字跑出去，回声会替它们登记——登记这种事，我从来不信是鬼做的。",
    "黑暗里有极细的气流，气流像蛇。蛇不必咬人，绕一圈就够。绕一圈你会明白：你不是来「看真相」的，你是来学会别乱喊的。",
    "我把绳结又检查一遍。检查是仪式，也是拖延。拖延在这里不是懦弱，是把决定再往嘴边推一寸——推一寸，有时就能少说一句会后悔的话。",
]


def pick_ext_pool(section: int, need: int, use_b: bool, seed_off: int = 0) -> str:
    pool = EXT_B if use_b else EXT_A
    n = len(pool)
    idx = (section * 23 + seed_off + 7) % n
    parts: list[str] = []
    step = 3 if use_b else 5
    used: set[int] = set()
    safety = 0

    def total_len() -> int:
        return sum(len(p) + 2 for p in parts) - 2 if parts else 0

    while total_len() < need and safety < 400:
        pid = idx % n
        if pid in used and len(used) < n:
            idx += step
            safety += 1
            continue
        used.add(pid)
        p = pool[pid]
        if not p.startswith("　　"):
            p = "　　" + p
        parts.append(p)
        idx += step
        safety += 1
        if len(used) >= n:
            used.clear()
    return "\n\n".join(parts)


def parse_header_body(text: str) -> tuple[str | None, str]:
    lines = text.splitlines()
    if lines and lines[0].startswith("#"):
        return lines[0], "\n".join(lines[1:]).strip()
    return None, text.strip()


def weave_expand(text: str, section: int, tmin: int) -> str:
    header, body = parse_header_body(text)
    if should_skip_section(section, len(text)):
        return text

    use_b = is_b_section(section)
    need = tmin - len(text) + 60
    if need <= 0:
        return text

    mid_ratio = 0.58
    mid_need = int(need * mid_ratio)
    end_need = need - mid_need

    mid_block = pick_ext_pool(section, mid_need, use_b, seed_off=0)
    mid_paras = [p.strip() for p in mid_block.split("\n\n") if p.strip()]

    paras = [p.strip() for p in body.split("\n\n") if p.strip()]
    if not paras:
        paras = [body] if body else ["　　"]

    ins_idx = max(1, min(len(paras) - 1, len(paras) // 3))
    new_paras = paras[:ins_idx] + mid_paras + paras[ins_idx:]
    body2 = "\n\n".join(new_paras)
    if header:
        out = header + "\n\n" + body2
    else:
        out = body2

    if len(out) < tmin:
        tail = pick_ext_pool(section, tmin - len(out) + 40, use_b, seed_off=11)
        out = out.rstrip() + "\n\n" + tail + "\n"

    while len(out) < tmin:
        out = out.rstrip() + "\n\n" + pick_ext_pool(section + 50, tmin - len(out) + 30, use_b, seed_off=19) + "\n"

    if len(out) > ABS_MAX:
        out = out[:ABS_MAX]  # 极端保护

    # 重场上沿：不强行裁切到 MAX，但若超过 ABS_MAX 已裁
    return out


def main() -> None:
    rows: list[str] = []
    rows.append("# 连载润色版 · 分层扩写后字数\n")
    rows.append("| 节 | 类型 | 目标下沿 | 扩写前 | 扩写后 | 文件名 |\n")
    rows.append("|:---:|:---|---:|---:|---:|:---|\n")

    for sec in range(1, 41):
        name = outfile_name(sec)
        path = OUT / name
        if not path.exists():
            rows.append(f"| {sec} | — | — | — | — | 缺失 {name} |\n")
            continue
        raw = path.read_text(encoding="utf-8")
        old_len = len(raw)
        typ = "重场" if sec in HEAVY_SECTIONS else "常规"
        if sec == 18:
            typ += "·18维持"
        tmin = target_min(sec)
        new_text = weave_expand(raw, sec, tmin)
        new_len = len(new_text)
        if new_text != raw:
            path.write_text(new_text, encoding="utf-8")
        rows.append(f"| {sec} | {typ} | {tmin} | {old_len} | {new_len} | {name} |\n")

    (OUT / "_tiered_len.md").write_text("".join(rows), encoding="utf-8")
    print("Wrote", OUT / "_tiered_len.md")


if __name__ == "__main__":
    main()
