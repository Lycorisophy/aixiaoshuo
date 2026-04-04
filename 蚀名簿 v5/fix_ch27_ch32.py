# -*- coding: utf-8 -*-
"""修复v8.7第27和32节的视角错误"""

with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.7.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 第27节修复
replacements_27 = [
    ('我一直以为"井底"是个地方。', '言临一直以为"井底"是个地方。'),
    ('直到那天我才明白，它更像一套系统', '直到那天言临才明白，它更像一套系统'),
    ('我心里一沉。\n\n这意味着', '言临心里一沉。\n\n言临意识到这意味着'),
    ('我心里一沉。\n\n言临意识到这意味着', '言临心里一沉。\n\n言临意识到这意味着'),
    ('我们沿着材料室侧墙摸过去', '他们沿着材料室侧墙摸过去'),
    ('我用指尖沾了一点，搓开，黏。', '言临用指尖沾了一点，搓开，黏。'),
]

# 第32节修复
replacements_32 = [
    ('我把手机递过去，顾清舟顺手点开相册', '言临把手机递过去，顾清舟顺手点开相册'),
    ('他把屏幕递回给我：', '他把屏幕递回给言临：'),
    ('他给了我一套很朴素的"旁证规则"', '他给了言临一套很朴素的"旁证规则"'),
    ('我看着那份清单，突然明白一件事：', '言临看着那份清单，突然明白一件事：'),
    ('不是我脑子里剩下多少。', '不是言临脑子里剩下多少。'),
    ('是我手里还能剩下多少纸。', '是言临手里还能剩下多少纸。'),
]

# 执行第27节替换
for old, new in replacements_27:
    if old in content:
        content = content.replace(old, new)
        print(f'已替换(27): {old[:30]}...')

# 执行第32节替换
for old, new in replacements_32:
    if old in content:
        content = content.replace(old, new)
        print(f'已替换(32): {old[:30]}...')

with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.7.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('\n修复完成！')
