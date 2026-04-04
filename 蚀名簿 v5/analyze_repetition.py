# -*- coding: utf-8 -*-
"""分析v8.7语义重复问题"""

with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.7.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找出章节标题位置
chapter_sections = []
for i, line in enumerate(lines):
    if line.startswith('## 第') and '节' in line:
        chapter_sections.append((i+1, line.strip()))

# 检测重复内容
def normalize_text(text):
    """标准化文本用于比较"""
    import re
    # 移除标点符号和多余空格
    text = re.sub(r'[，。、！？；：「」『』""''【】（）]', '', text)
    text = re.sub(r'\s+', '', text)
    return text

# 找出章节
def get_section(line_num):
    for i, (loc, title) in enumerate(chapter_sections):
        if loc <= line_num:
            current_section = title
    return current_section if 'current_section' in dir() else '未知'

# 检测相邻或相近行的重复
repetition_issues = []
for i in range(len(lines) - 1):
    line1 = lines[i].strip()
    line2 = lines[i+1].strip()
    
    # 跳过空行
    if not line1 or not line2:
        continue
    
    # 跳过章节标题
    if line1.startswith('## 第'):
        continue
    
    # 规范化后比较
    norm1 = normalize_text(line1)
    norm2 = normalize_text(line2)
    
    # 跳过太短的行
    if len(norm1) < 10 or len(norm2) < 10:
        continue
    
    # 检测重复
    if norm1 == norm2:
        section = get_section(i+1)
        repetition_issues.append((i+1, '完全重复', line1[:60], line2[:60], section))
    elif len(norm1) > 0 and len(norm2) > 0:
        # 检测高度相似（80%以上相同）
        shorter = min(len(norm1), len(norm2))
        longer = max(len(norm1), len(norm2))
        if shorter / longer > 0.85:
            # 检查是否是一行被分成了两行
            if norm1 in norm2 or norm2 in norm1:
                section = get_section(i+1)
                repetition_issues.append((i+1, '高度相似(拆分?)', line1[:60], line2[:60], section))

# 检测连续诗行的重复
poetry_repetitions = []
for i in range(len(lines) - 4):
    line1 = lines[i].strip()
    line2 = lines[i+1].strip()
    line3 = lines[i+2].strip()
    line4 = lines[i+3].strip()
    
    # 检测连续4行诗重复
    if '雨丝' in line1 and '雨丝' in line3:
        if abs(len(line1) - len(line3)) < 5:
            section = get_section(i+1)
            poetry_repetitions.append((i+1, line1[:50], line3[:50], section))

print(f'=== 语义重复分析 ===')
print(f'总行数: {len(lines)}')
print(f'\\n=== 完全重复或高度相似 ===')
for loc, issue_type, text1, text2, section in repetition_issues[:30]:
    print(f'行{loc} [{issue_type}] [{section}]')
    print(f'  原文1: {text1}')
    print(f'  原文2: {text2}')
    print()

print(f'\\n=== 诗行重复 ===')
for loc, text1, text2, section in poetry_repetitions[:20]:
    print(f'行{loc} [{section}]')
    print(f'  行1: {text1}')
    print(f'  行2: {text2}')
    print()

print(f'\\n共发现约{len(repetition_issues)}处重复问题')
print(f'共发现约{len(poetry_repetitions)}处诗行重复')

# 保存详细分析
with open(r'C:\project\aixiaoshuo\蚀名簿 v5\repetition_analysis.txt', 'w', encoding='utf-8') as f:
    f.write(f'=== 语义重复分析 ===\n')
    f.write(f'总行数: {len(lines)}\n')
    f.write(f'共发现约{len(repetition_issues)}处重复问题\n')
    f.write(f'共发现约{len(poetry_repetitions)}处诗行重复\n\n')
    f.write('=== 完全重复或高度相似(前50) ===\n')
    for loc, issue_type, text1, text2, section in repetition_issues[:50]:
        f.write(f'行{loc} [{issue_type}] [{section}]\n')
        f.write(f'  原文1: {text1}\n')
        f.write(f'  原文2: {text2}\n\n')
    f.write('\n=== 诗行重复(前30) ===\n')
    for loc, text1, text2, section in poetry_repetitions[:30]:
        f.write(f'行{loc} [{section}]\n')
        f.write(f'  行1: {text1}\n')
        f.write(f'  行2: {text2}\n\n')

print(f'\n详细分析已保存到 repetition_analysis.txt')
