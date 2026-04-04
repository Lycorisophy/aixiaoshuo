# -*- coding: utf-8 -*-
"""统计严重省略号滥用"""

with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.7.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 检测连续字……格式
severe_abuse = []
for i, line in enumerate(lines):
    line_stripped = line.strip()
    count = line_stripped.count('……')
    if count >= 3 and '字' in line_stripped:
        severe_abuse.append((i+1, count, line_stripped[:80]))

print('=== 严重滥用：单行>=3个省略号且含字 ===')
print(f'共发现 {len(severe_abuse)} 处')
for loc, count, text in severe_abuse[:50]:
    print(f'行{loc} ({count}个): {text[:60]}')

# 按章节统计
chapter_counts = {}
current_section = '未知'
for i, line in enumerate(lines):
    if line.startswith('## 第') and '节' in line:
        current_section = line.strip()
        chapter_counts[current_section] = 0

for loc, count, text in severe_abuse:
    for section in chapter_counts:
        section_num = int(section.split('第')[1].split('节')[0].strip())
        if section_num >= 1:
            # 简单判断所属章节
            pass
