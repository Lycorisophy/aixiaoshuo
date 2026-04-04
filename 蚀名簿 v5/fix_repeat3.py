# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 使用多个replace操作
content = content.replace('"失踪。"\n\n\n"什么意思？"\n\n\n"出什么事？"', '"失踪。"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
