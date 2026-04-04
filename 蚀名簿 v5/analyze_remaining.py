# -*- coding: utf-8 -*-
"""分析剩余的言临"""
with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.8.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找出第四章范围
start = end = None
for i, line in enumerate(lines):
    if '## 第 25 节' in line:
        start = i
    elif '## 第 33 节' in line:
        end = i
        break

# 统计剩余言临类型
keep = []  # 对话中的名字
fix = []   # 叙述中的言临

for i in range(start, end):
    if '言临' in lines[i]:
        line = lines[i].strip()
        # 判断是哪种类型
        if '"言临"' in line or '言临。"' in line or '言临，' in line or '言临？' in line or '悟缘突然说' in line:
            keep.append((i+1, line[:70]))
        elif '秦观、言临' in line:
            keep.append((i+1, line[:70]))
        else:
            fix.append((i+1, line[:70]))

print(f'=== 应保留（对话中的名字）: {len(keep)}处 ===')
for loc, text in keep[:15]:
    print(f'行{loc}: {text}')

print()
print(f'=== 应修复（叙述中的）: {len(fix)}处 ===')
for loc, text in fix[:30]:
    print(f'行{loc}: {text}')
