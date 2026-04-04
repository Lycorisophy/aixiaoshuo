# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 删除第250行开始的重复块
# 第250行（索引249）是重复的"什么意思？"
new_lines = []
skip = 0

for i, line in enumerate(lines):
    if i == 249:  # 第250行
        # 开始跳过，直到跳过"什么意思？"+空行+"出什么事？"
        skip = 1
        continue
    if skip > 0:
        if '"出什么事？"' in line:
            skip = 2
            continue
        elif skip == 2 and '"失踪。"' in line:
            skip = 0
            continue
        elif skip == 1 and line.strip() == '':
            continue
        elif skip == 1:
            skip = 0
    
    new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'当前行数: {len(new_lines)}')
