# -*- coding: utf-8 -*-
"""修复第27节开头的我一直以为"""

with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.7.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 查找并替换
target = '我一直以为"井底"是个地方。'
replacement = '言临一直以为"井底"是个地方。'

if target in content:
    content = content.replace(target, replacement, 1)
    print(f'已替换第27节开头')
else:
    print('未找到目标字符串')

with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.7.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('完成')
