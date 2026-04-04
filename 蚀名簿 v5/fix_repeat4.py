# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 清理所有类似重复块
replacements = [
    ('"失踪。"\n\n\n"什么意思？"\n\n\n"出什么事？"',
     '"失踪。"'),
    ('"失踪。"\n\n"什么意思？"\n\n"出什么事？"',
     '"失踪。"'),
    ('"出什么事？"\n\n"失踪。"\n\n\n"什么意思？"\n\n\n"出什么事？"\n\n"失踪。"',
     '"出什么事？"\n\n"失踪。"'),
]

count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'完成 {count} 处替换')
