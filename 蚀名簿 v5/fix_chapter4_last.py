# -*- coding: utf-8 -*-
"""
精确修复v8.8第四章中剩余的"言临"
保留对话中的名字，只修复叙述中的"言临"
"""

with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.8.md', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# 找出第四章的起始和结束位置
chapter4_start = None
chapter4_end = None

for i, line in enumerate(lines):
    if '## 第 25 节' in line:
        chapter4_start = i
    elif '## 第 33 节' in line:
        chapter4_end = i
        break

if chapter4_end is None:
    chapter4_end = len(lines)

print(f'第四章范围: 行{chapter4_start+1} - 行{chapter4_end}')

fixes = []
for i in range(chapter4_start, chapter4_end):
    line = lines[i]
    
    # 需要修复的第三人称叙述模式
    patterns = [
        ('言临知道', '我知道'),
        ('言临停住了', '我停住了'),
        ('言临不知道', '我不知道'),
        ('言临看到了', '我看到了'),
        ('言临走过去', '我走过去'),
        ('言临坐下来', '我坐下来'),
        ('言临站住了', '我站住了'),
        ('言临慢慢说', '我慢慢说'),
        ('言临低声说', '我低声说'),
        ('言临抬头', '我抬头'),
        ('言临伸手', '我伸手'),
        ('言临喃喃自语', '我喃喃自语'),
        ('久到言临觉得', '久到我觉得'),
        # 特殊处理"那个写下秦观、言临"中的言临需要保留
    ]
    
    for old, new in patterns:
        if old in line:
            lines[i] = line.replace(old, new)
            fixes.append(f'行{i+1}: {old} -> {new}')

# 保存
output = '\n'.join(lines)
with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.8.md', 'w', encoding='utf-8') as f:
    f.write(output)

print(f'\n修复完成，共 {len(fixes)} 处:')
for fix in fixes:
    print(f'  {fix}')

# 统计第四章中剩余的"言临"
print('\n=== 第四章中剩余的"言临"统计 ===')
remaining = []
for i in range(chapter4_start, chapter4_end):
    if '言临' in lines[i]:
        remaining.append((i+1, lines[i].strip()))

print(f'剩余 {len(remaining)} 处')
