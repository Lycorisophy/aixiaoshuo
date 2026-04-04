# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 替换重复的对话块
old = '''"失踪。"


"什么意思？"


"出什么事？"""

new = '''"失踪。"'''

if old in content:
    content = content.replace(old, new, 1)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('已替换')
else:
    print('未找到')
