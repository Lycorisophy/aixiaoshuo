# -*- coding: utf-8 -*-
"""分析v8.7省略号使用模式"""

with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.7.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找出章节标题位置
chapter_sections = []
for i, line in enumerate(lines):
    if line.startswith('## 第') and '节' in line:
        chapter_sections.append((i+1, line.strip()))

# 找出滥用模式：字……字……格式
abuse_patterns = []
for i, line in enumerate(lines):
    # 检测"字……字……"格式
    if '字……' in line:
        abuse_patterns.append((i+1, '字……重复', line.strip()))
    # 检测连续多行省略号
    if line.strip() == '……' or line.strip() == '……' or '…………' in line:
        abuse_patterns.append((i+1, '纯省略号行', line.strip()))

# 检测同一行内省略号过多（如连续3个以上省略号）
excessive_ellipsis = []
for i, line in enumerate(lines):
    count = line.count('……')
    if count >= 5:
        excessive_ellipsis.append((i+1, f'{count}个省略号', line.strip()[:80]))

print(f'=== 省略号滥用分析 ===')
print(f'总行数: {len(lines)}')
print(f'章节数: {len(chapter_sections)}')
print(f'\\n=== 字……重复模式 ===')
for loc, pattern, text in abuse_patterns[:30]:
    print(f'行{loc}: {text[:60]}')

print(f'\\n=== 纯省略号行 ===')
pure_count = 0
for loc, pattern, text in abuse_patterns:
    if text.strip() == '……' or '…………' in text:
        pure_count += 1
print(f'纯省略号行数量: {pure_count}')

print(f'\\n=== 单行过多省略号(>=5个) ===')
for loc, count, text in excessive_ellipsis[:20]:
    print(f'行{loc}: {count} - {text[:50]}')

# 保存详细分析
with open(r'C:\project\aixiaoshuo\蚀名簿 v5\ellipsis_analysis.txt', 'w', encoding='utf-8') as f:
    f.write(f'=== 省略号滥用分析 ===\\n')
    f.write(f'总行数: {len(lines)}\\n')
    f.write(f'章节数: {len(chapter_sections)}\\n\\n')
    f.write('=== 字……重复模式(前50) ===\\n')
    for loc, pattern, text in abuse_patterns[:50]:
        f.write(f'行{loc}: {text}\\n')
    f.write(f'\\n=== 单行过多省略号(>=5个)(前30) ===\\n')
    for loc, count, text in excessive_ellipsis[:30]:
        f.write(f'行{loc}: {count} - {text}\\n')

print(f'\\n详细分析已保存到 ellipsis_analysis.txt')
