# -*- coding: utf-8 -*-
"""
继续修复v8.8第四章中的"他"为"我"
第26节末尾及其他位置存在用"他"指代言临的问题
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
    original = line
    
    # 第26节末尾附近的"他"问题
    # 这些"他"在上下文中明显指代言临（第一人称"我"）
    
    # 1. "他走出衔霜楼" -> "我走出衔霜楼"
    if '他走出衔霜楼' in line:
        lines[i] = line.replace('他走出衔霜楼', '我走出衔霜楼')
        fixes.append(f'行{i+1}: 他走出衔霜楼 -> 我走出衔霜楼')
    
    # 2. "他喃喃自语" -> "我喃喃自语"
    if '他喃喃自语' in line:
        lines[i] = line.replace('他喃喃自语', '我喃喃自语')
        fixes.append(f'行{i+1}: 他喃喃自语 -> 我喃喃自语')
    
    # 3. "他继续往前走" -> "我继续往前走"
    if '他继续往前走' in line:
        lines[i] = line.replace('他继续往前走', '我继续往前走')
        fixes.append(f'行{i+1}: 他继续往前走 -> 我继续往前走')
    
    # 4. "但他知道一件事" -> "但我知道一件事"
    if '但他知道一件事' in line:
        lines[i] = line.replace('但他知道一件事', '但我知道一件事')
        fixes.append(f'行{i+1}: 但他知道一件事 -> 但我知道一件事')
    
    # 5. "他不会去秦氏旧居" -> "我不会去秦氏旧居"
    if '他不会去秦氏旧居' in line:
        lines[i] = line.replace('他不会去秦氏旧居', '我不会去秦氏旧居')
        fixes.append(f'行{i+1}: 他不会去秦氏旧居 -> 我不会去秦氏旧居')
    
    # 6. "他会去一个能让他找到答案的地方" -> "我会去一个能让我找到答案的地方"
    if '他会去一个能让他找到答案的地方' in line:
        lines[i] = line.replace('他会去一个能让他找到答案的地方', '我会去一个能让我找到答案的地方')
        fixes.append(f'行{i+1}: 他会去 -> 我会去')
    
    # 7. "一个藏着所有败者的地方" -> "一个藏着所有败者的地方" (无需修改)
    
    # 8. "因为她突然意识到" -> "因为我突然意识到"
    if '因为她突然意识到' in line:
        lines[i] = line.replace('因为她突然意识到', '因为我突然意识到')
        fixes.append(f'行{i+1}: 因为她突然意识到 -> 因为我突然意识到')
    
    # 9. "他会想起" -> "我会想起"
    if '他会想起' in line:
        lines[i] = line.replace('他会想起', '我会想起')
        fixes.append(f'行{i+1}: 他会想起 -> 我会想起')

# 保存
output = '\n'.join(lines)
with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.8.md', 'w', encoding='utf-8') as f:
    f.write(output)

print(f'\n修复完成，共 {len(fixes)} 处:')
for fix in fixes:
    print(f'  {fix}')
