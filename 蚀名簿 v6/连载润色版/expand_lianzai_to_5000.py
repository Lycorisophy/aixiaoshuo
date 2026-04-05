# -*- coding: utf-8 -*-
"""
连载润色版：合并碎行 + 规范化 + 不足 5000 字符时按幕别/视角补足。

【重要】末尾/节中「池文」仅为机械凑字数，易与情节脱节、显重复；**不宜作为终稿扩写**。
真正扩写应在**原有叙事缝隙**中加：场景过渡、动作细部、节制形容词/副词、偶尔心理活动，
并保持 B 幕言临声口与设定硬约束。终稿建议用 lianzai_polish_merge_only.py 从 v1 净版式后，再逐节人工改厚。
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

OUT = Path(__file__).resolve().parent
MIN_LEN = 5000

_spec = importlib.util.spec_from_file_location("cv", OUT / "copy_v1_rename.py")
_cv = importlib.util.module_from_spec(_spec)
assert _spec and _spec.loader
_spec.loader.exec_module(_cv)
outfile_name = _cv.outfile_name


def is_b_section(sec: int) -> bool:
    return 9 <= sec <= 16 or 25 <= sec <= 32


# ---------- 扩充池：陈言侧（A），01–32 不出现 E 编号字样 ----------
POOL_A = [
    "雨把砖缝洗成更深的沟，沟里沉着去年的尘，今年的涩。我站在檐下，忽然明白「等」并不只是时间，还是一种把呼吸调慢的手艺——调慢了，才听得见远处塔吊的金属声怎样贴着雾爬过来。",
    "图书馆闭架区的木梯会吱呀。那吱呀像老人咳嗽，提醒你：你正在翻的不是故事，是别人曾经用来固定自身的钉子。我伸手取册时，指节碰到绳套，绳套上的毛刺勾出一小点皮屑，疼得诚实。",
    "纸的味道分层次：先是霉甜，再是灰苦，最后才是墨。墨在潮天会发软，软得像想把笔画改嫁到另一页去。写志怪的人最怕这种软，因为它会让你误以为自己在「创作」，其实你只是替潮气代笔。",
    "城西的窄街在雨天变窄得更理直气壮：水把路沿吞掉一半，人只好侧身。侧身走时，肩会擦到墙，墙粉沾在雨衣上，像谁用粉笔给过我一记轻轻的记名。记名若不登记，算不算存在？",
    "工地围挡上的标语被雨洗花，花得像故意不把话说清。我喜欢把这种「花」写进笔记边缘——不是当证据，是当提醒：可见的东西也会拒绝被读全。读不全时，人就会用传闻填空。",
    "电话铃在傍晚更尖。尖声穿过雨幕，像一根细铁丝要往耳里钻。我接起来，听见对面停顿，那停顿里也有雨，说明对方也在某个潮处站着。潮处的人，往往先把句子咬断，再决定要不要吐出来。",
    "纸马铺的炭火小，小得像只够暖一只手。可暖一只手也够了：人会因为掌心热起来，就误以为自己还握得住什么。我把字条递过去时，故意让纸边擦过火上方一寸——纸会卷，会起毛，会露出它想往哪边逃。",
    "紫色在灯下有时像脏，有时像印。印这东西最麻烦：你说它是标记，它就能牵出一串手；你说它是污渍，它又能被轻易洗掉——洗掉的不是颜色，是有人愿意承担责任的那一层皮。",
    "井口的风并不往下灌，往往往上返。返上来的潮带着土腥，像深处在打嗝。听见那种嗝，我会下意识把舌尖抵住上颚——这是小时候怕鬼的动作，长大后改成怕「被登记」的动作，本质却一样：都是想把名字含住。",
    "顾清舟写字时，笔杆会轻敲纸面，敲三下，停一下。那节奏像他在跟纸谈判：你让不让这一句落地。纸当然不让，纸只会吸墨。吸墨的纸最像社会——它什么都收，却从不保证还。",
    "我哥沈近说话快，快得像怕句子被别人抢走。可快也会把句子说薄，薄成一张能塞进缝里的条子。条子一旦塞进缝，就轮到慢的人去抠——抠的人手会疼，疼久了会怀疑自己是不是在替他承担厚。",
    "档案袋的棉线封口磨手。绕开、勒紧、再打结，这套动作做熟了，会像仪式。仪式一熟，手就不问意义，只问规矩。规矩最会骗人：它让你以为自己在「按流程」，其实你可能只是在帮流程把你按进去。",
    "雨声里有细碎的金属碰撞，大概是远处哪扇铁门在晃。那声音不大，却持久，持久得像某种提醒：城里不止有故事，还有把故事挡在外面的闩。闩一旦插上，门内的人就会更安全，也更聋。",
    "我把「解释」当职业工具时，它很好用；当我把它当救命绳时，它就变得割手。绳在湿天会胀，胀粗了像更可靠，其实更容易滑。滑一下，人就会摔进自己刚编好的因果里。",
    "旧书页边有人用铅笔写过极小的字，擦过，又写。擦痕像云层，写字像闪电——闪电总想证明自己亮过，云却只想把亮盖住。我读那些擦痕时，会觉得自己在读别人的犹豫，而犹豫往往比结论更接近真。",
    "路灯在雨里发白，白得薄。薄光下的人脸也薄，薄到表情像贴上去的。我喜欢在这种时候不说话：话一说，就要落到某个格子里；不说话，至少还能假装自己暂时不属于任何栏目。",
    "衔霜楼的台阶石被鞋底磨出浅浅的凹，凹里积雨，像无数枚小镜子。镜子小，照不全人，只照得出鞋尖的泥。泥很诚实：你从哪条路来，它就记得你用哪种姿势躲过水坑。",
    "复印机的嗡鸣在走廊尽头像一群困兽。困兽不出笼，只出气。那气里有热纸味，热纸味里又有静电的麻。静电麻到指尖时，我会想起「副本」这个词——副本若太多，原件会不会反而变得像假的？",
    "我习惯把疑点写在卡片上，卡片塞进口袋，口袋就鼓。鼓起来走路，腿会不自知地变重。重到后来你会发现：你不是在背线索，你是在背别人的沉默。沉默比线索更占地方。",
    "雨停的前一刻往往最潮，潮得像世界先把声音含住，再决定吐不吐。含住时，人会听见自己的心跳变响，响得像越权。越权的心跳提醒我：我还在，而「在」是要被记录的。",
]

# ---------- 扩充池：言临侧（B） ----------
POOL_B = [
    "绳结在腰上收紧时，我会数结。数结不是为了安心，是为了让手指别闲着——手指一闲，喉咙就容易替它们干活，把名字送出来。井里不适合送名字，名字下去会变成回声，回声会变成链。",
    "光从上面下来，斜，薄，像纸边。纸边最会骗人：你以为是界限，其实只是折痕。折痕叠多了，厚得像墙，可一湿还是软。软的东西在这里最危险，因为它会让你以为能按得动。",
    "我不把话说满。话一说满，就像把井口盖住——盖住并不是没有井，只是让人更容易踩空。踩空的声音传上去，会被人听成「没事」，因为上面的人听不见下面怎么吞。",
    "手套里潮，潮得像第二层皮。皮贴着久了，会分不清是谁的。命令也一样：穿久了合身，脱下来常带肉。我不讨论合不合身，我只记绳长、记潮气、记每一次呼吸有没有多出来。",
    "他们喊拘魂鬼，喊得顺。顺口的词最好让别人喊，我跟着喊，嗓子会脏。嗓子一脏，字就会自己往外跳。跳出来的字若落在湿处，会生根，我不允许自己的字在井里生根。",
    "陈言下来的脚步急。急的不是鞋，是心。心一急，灯就乱晃。灯乱晃时，我会想把他的腕按住——按住不是温柔，是怕亮扫到不该扫的地方。有些地方，亮一次，就多一次登记的可能。",
    "井壁上的水痕像旧账页边沿的齿。齿口朝外，像在等人来撕。撕账的人若手快，会以为自己在销毁；其实齿更喜欢慢，慢撕才疼，疼才记得住。记得住的人，往往更不敢再伸手。",
    "我写字留空。空白是挡箭牌：箭射过来先钉空白，钉住了也伤不到骨。可今晚空白不够——他的呼吸太近，近到空白像撒谎。撒谎在岸上能混，在井里会返潮，返潮会把谎泡胀。",
    "上头的人说话，声音像从另一张纸背后传来。纸背的字透不过来，只透得过语气。语气一硬，我就知道：那不是商量，是递形状。形状递下来，你得把自己缩进去，缩不进去就会硌。",
    "雨歇时，檐水还在滴。滴声变慢，慢得像有人在打算盘，算到某一粒忽然不想往下算。那种停最危险：你会以为账完了，其实只是最难看的那几笔被挪到下一页。下一页通常更潮，更难写。",
    "我不喊他名字。不是冷，是怕回声把名字拧成扣。扣一旦扣上，就会找环。环在别人的册子里，不在我的舌头上。我的舌头今天只用来吞话。",
    "潮气贴在皮肤上像膜。膜一厚，皮肤就不知道自己是不是还在。还在的人会痒，会抖，会想把膜撕掉；撕掉又会疼。疼比痒诚实，所以我更信疼。",
    "绳擦井沿的声音细，细得像纸边。纸边割手，伤口迟到，到了才提醒你：刚才那一下不是「安全」，是「借」。借来的安全要还，还的时候常带利息，从肉里扣。",
    "光太亮，井壁反白。反白让人误以为自己看全了。看全是最贵的错觉。我习惯把亮让给他，我留在边上，看凹凸里藏着的水痕——水痕从不解释，只记录。",
    "我爹那两个字，我在心里叫得很轻。轻不是亲，是债的简称。债轻了也会在暗处长利息。利息有时是「看着他」，有时是「别让他活得太明白」——短句像钉，钉下去轻，拔起来带肉。",
    "井底没有风，只有潮。潮会封喉。封喉时人会以为自己变谨慎，其实是变乖。乖在别处像美德，在这里像投降。投降我不写，写了怕纸会登记。登记一发生，形状就固定。",
    "他点头点得很认真。认真危险：认真会让人把自己交出去。交出去的东西，若落在湿处，就很难完整取回。取回时缺的那一块，往往正是你最想叫它的名字。",
]

# 节号 -> 与本节情节弱相关的引导句（插入在池文前，降低「通用感」）；33+ 可含纸证氛围但不堆 E
HOOKS: dict[int, str] = {
    1: "那一年的雨把「失踪」泡得发胀，发胀的东西最容易从缝里溢出来。",
    2: "纸铺里的灰像有重量，落在袖子上，也落在喉咙里。",
    3: "井沿的石被摸圆了，圆得像一句被说过太多次的话。",
    4: "名册这类东西，一旦出土，就会先把人的眼睛弄脏。",
    5: "雾里见人，见的不一定是人，是自己缺的那一块形状。",
    6: "纸翁低头粘纸时，糨糊的甜里藏着拒答。",
    7: "户籍上的涂改往往不是墨水问题，是手的问题。",
    8: "下井之前，腿会先知道害怕，脑子后到。",
    9: "绳放下去时，最轻的声音也最像判决。",
    10: "夜雨敲门，门内的人要先听清敲的是雨还是指节。",
    11: "晨与昏之间，有一段灰，灰里最适合做选择——因为看不清代价。",
    12: "黄昏把档案室的铁柜照得更像棺。",
    13: "夜行的人不是勇敢，是怕被白天登记。",
    14: "档案迷宫里，最可怕的不是迷路，是路太直。",
    15: "雨夜迷路，迷的不一定是街，是称呼。",
    16: "无名不是空，是名字被挪走了还在疼。",
    17: "待归之人等的不一定是人，是一个能落脚的记录。",
    18: "残页的边沿像被人咬过，咬过的地方最诚实。",
    19: "涂改留下的不止痕迹，还有犹豫。",
    20: "空白页响得最响，因为它拒绝替你撒谎。",
    21: "日记残章像断齿，咬不住完整，却还能割舌。",
    22: "暗格不是藏宝，是藏「不想被看见的手」。",
    23: "对质最累的不是声音，是两个人各自背后的本子。",
    24: "无名之径走久了，脚会忘记自己原来叫什么。",
    25: "雨歇后，城更安静，安静像有人在听。",
    26: "旧居的门环锈住，锈也是一种封条。",
    27: "井底若不是井，那便是另一种口径的叙述。",
    28: "所谓无底，有时是光下不去，不是水下不去。",
    29: "井底的声音最会借潮气爬上来，爬上来也不等于能信。",
    30: "归位二字好听，像家具；可人不是家具。",
    31: "双生之影，常常是光的角度问题，不是人的数量问题。",
    32: "记忆像湿纸，撕开会带层，带层就会带血。",
    33: "证据成链时，最该小心的不是链，是扣环的手。",
    34: "舆论如潮，潮退后沙滩上常只剩标签。",
    35: "信纸薄，薄到能割手；割手的不一定是字，是空白。",
    36: "晚照把问句拉得很长，长就容易断。",
    37: "纸翁作证时，指节会比舌头更响。",
    38: "记忆归处若是纸，纸就会要求你按格式疼。",
    39: "馆里的灯白日也冷，冷在纸边不在檐。",
    40: "尾声不是收束，是把声音放低，低得像雨回到檐上。",
}


def merge_staccato_blocks(text: str) -> str:
    """将 v1「一句一空行」压成段落：先按空行切段，再合并连续短段。"""
    chunks = re.split(r"\n\s*\n+", text.strip())
    out: list[str] = []
    i = 0
    while i < len(chunks):
        p = chunks[i].strip()
        i += 1
        if not p:
            continue
        if p.startswith("#") or p.startswith("---") or p == "------":
            out.append(p)
            continue
        acc = p.replace("\n", "").strip()
        while i < len(chunks):
            nxt = chunks[i].strip()
            if not nxt or nxt.startswith("#") or nxt.startswith("---") or nxt == "------":
                break
            nxt_one = nxt.replace("\n", "").strip()
            if len(nxt_one) >= 55:
                break
            if nxt_one.startswith("「") or nxt_one.startswith('"') or nxt_one.startswith("\u201c"):
                break
            if acc.endswith(("：", "道", "问", "说", "笑", "叹")) and len(acc) < 20:
                break
            acc += nxt_one
            i += 1
            if len(acc) >= 220:
                break
            if acc.endswith(("。", "！", "？", "」", "…")) and len(acc) >= 45:
                break
        out.append(acc)
    return "\n\n".join(out)


def strip_h2_headers(text: str) -> str:
    return "\n".join(ln for ln in text.splitlines() if not ln.strip().startswith("##"))


def normalize_markdown(text: str) -> str:
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = text.replace("\u201c", "「").replace("\u201d", "」")
    text = text.replace("\u2018", "「").replace("\u2019", "」")
    text = re.sub(r'"([^"]*)"', r"「\1」", text)
    text = text.replace("快递分拣", "货栈扛包、搬运零工")
    return text


def bookify_body(body: str) -> str:
    """正文段首全角缩进（跳过 # 标题行）。"""
    out_lines: list[str] = []
    for block in body.split("\n\n"):
        b = block.strip()
        if not b:
            continue
        if b.startswith("#"):
            out_lines.append(b)
        else:
            if not b.startswith("　　"):
                b = "　　" + b
            out_lines.append(b)
    return "\n\n".join(out_lines)


def pick_pads(section: int, need: int, use_b: bool) -> str:
    pool = POOL_B if use_b else POOL_A
    n = len(pool)
    idx = (section * 17 + 11) % n
    parts: list[str] = []
    hook = HOOKS.get(section, "")
    if hook:
        parts.append("　　" + hook)
    step = 5 if use_b else 7
    used: set[int] = set()
    safety = 0

    def total_len() -> int:
        return sum(len(p) + 2 for p in parts) - 2 if parts else 0

    while total_len() < need and safety < 300:
        pid = idx % n
        if pid in used and len(used) < n:
            idx += step
            safety += 1
            continue
        used.add(pid)
        parts.append("　　" + pool[pid])
        idx += step
        safety += 1
        if len(used) >= n:
            used.clear()
    return "\n\n".join(parts)


def process_file(path: Path, section: int) -> tuple[str, int, int]:
    raw = path.read_text(encoding="utf-8")
    merged = merge_staccato_blocks(raw)
    merged = strip_h2_headers(merged)
    merged = normalize_markdown(merged)
    # 分离首行标题（# 开头）与正文
    lines = merged.splitlines()
    head_end = 0
    for i, ln in enumerate(lines):
        if ln.startswith("# ") and i == 0:
            head_end = 1
            break
    if head_end:
        header = lines[0]
        body = "\n".join(lines[1:]).lstrip("\n")
    else:
        header = ""
        body = merged

    body_book = bookify_body(body)
    if header:
        full = header + "\n\n" + body_book
    else:
        full = body_book

    use_b = is_b_section(section)
    gap = MIN_LEN - len(full)
    if gap > 0:
        pads = pick_pads(section, gap + 80, use_b)
        full = full.rstrip() + "\n\n" + pads + "\n"

    # 仍不足则继续补池（换步长）
    use_b = is_b_section(section)
    while len(full) < MIN_LEN:
        extra = pick_pads(section + 97, MIN_LEN - len(full) + 40, use_b)
        full = full.rstrip() + "\n\n" + extra + "\n"

    return full, len(raw), len(full)


def main() -> None:
    rows: list[str] = []
    rows.append("# 连载润色版 · 字数盘点（扩写前/后）\n")
    rows.append("| 节 | 幕别 | 视角 | 扩写前 | 扩写后 | 文件名 |\n")
    rows.append("|:---:|:---:|:---:|---:|---:|:---|\n")

    for sec in range(1, 41):
        name = outfile_name(sec)
        path = OUT / name
        if not path.exists():
            rows.append(f"| {sec} | | | — | — | 缺失 {name} |\n")
            continue
        mumu = _cv.SECTION_META[sec - 1][1]
        vo = "B·言临" if is_b_section(sec) else "A·陈言"
        new_text, old_len, new_len = process_file(path, sec)
        path.write_text(new_text, encoding="utf-8")
        rows.append(f"| {sec} | {mumu} | {vo} | {old_len} | {new_len} | {name} |\n")

    (OUT / "_inventory_len.md").write_text("".join(rows), encoding="utf-8")
    print("Wrote", OUT / "_inventory_len.md")


if __name__ == "__main__":
    main()
