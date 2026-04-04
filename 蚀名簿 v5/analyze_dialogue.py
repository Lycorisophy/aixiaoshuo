# -*- coding: utf-8 -*-
"""分析v8.7不明对话问题"""

with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.7.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找出章节标题位置
chapter_sections = []
for i, line in enumerate(lines):
    if line.startswith('## 第') and '节' in line:
        chapter_sections.append((i+1, line.strip()))

# 不明对话检测：连续2行以上对话，没有说话人说明
def is_dialogue(line):
    """判断是否为对话行"""
    stripped = line.strip()
    # 以引号开头或结尾的可能是对话
    if stripped.startswith('"') or stripped.endswith('"') or stripped.startswith('"') or stripped.endswith('"'):
        return True
    if stripped.startswith('"') or stripped.endswith('"'):
        return True
    # 以对话符号开头
    if '“' in line or '”' in line:
        return True
    return False

def has_speaker(line):
    """判断是否有说话人说明"""
    # 常见说话人模式：XXX说、XXX道、XXX问、XXX答、XXX喊、XXX低声道等
    speaker_patterns = ['说：', '说"',
                       '道："', '道："',
                       '问："', '问："',
                       '答："', '答："',
                       '喊："', '喊："',
                       '低声道', '低声说',
                       '叹了口气', '顿了顿', '点了点头', '摇',
                       '看着我', '看着', '转向',
                       '突然', '突然说']
    for pattern in speaker_patterns:
        if pattern in line:
            return True
    return False

# 分析连续对话
dialogue_issues = []
i = 0
current_section = 1
in_dialogue_block = False
dialogue_block_start = 0
consecutive_dialogues = 0

while i < len(lines):
    line = lines[i]
    
    # 检测章节变化
    for j, (loc, title) in enumerate(chapter_sections):
        if loc == i + 1:
            current_section = title
            break
    
    stripped = line.strip()
    
    if is_dialogue(line):
        if not has_speaker(line):
            consecutive_dialogues += 1
            if consecutive_dialogues >= 2:
                # 记录连续不明对话
                if not dialogue_issues or dialogue_issues[-1][0] != dialogue_block_start:
                    dialogue_issues.append((dialogue_block_start, consecutive_dialogues, current_section))
            else:
                dialogue_block_start = i + 1
        else:
            consecutive_dialogues = 0
    else:
        consecutive_dialogues = 0
    
    i += 1

# 输出结果
print(f'=== 不明对话分析 ===')
print(f'总行数: {len(lines)}')
print(f'章节数: {len(chapter_sections)}')
print(f'\\n=== 连续对话无说话人(>=2行) ===')
issue_count = 0
for loc, count, section in dialogue_issues[:50]:
    print(f'章节: {section}')
    print(f'  位置: 行{loc}附近，连续{count}行无说话人')
    issue_count += 1

print(f'\\n共发现约{len(dialogue_issues)}处不明对话')

# 保存详细分析
with open(r'C:\project\aixiaoshuo\蚀名簿 v5\dialogue_analysis.txt', 'w', encoding='utf-8') as f:
    f.write(f'=== 不明对话分析 ===\n')
    f.write(f'总行数: {len(lines)}\n')
    f.write(f'共发现约{len(dialogue_issues)}处不明对话\n\n')
    f.write('=== 连续对话无说话人(>=2行)(前100) ===\n')
    for loc, count, section in dialogue_issues[:100]:
        f.write(f'章节: {section}\n')
        f.write(f'  位置: 行{loc}附近，连续{count}行无说话人\n\n')

print(f'\n详细分析已保存到 dialogue_analysis.txt')
