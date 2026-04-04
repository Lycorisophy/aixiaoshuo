# -*- coding: utf-8 -*-
"""
继续修复v8.8第四章中所有剩余的"言临"
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

# 修复所有剩余的"言临"为"我"
fixes = []
for i in range(chapter4_start, chapter4_end):
    line = lines[i]
    
    # "言临的" -> "我的" (但保留对话中的名字)
    if '言临的' in line:
        lines[i] = line.replace('言临的', '我的')
        fixes.append(f'行{i+1}: 言临的 -> 我的')
    
    # "言临转身就走" -> "我转身就走"
    if '言临转身就走' in line:
        lines[i] = line.replace('言临转身就走', '我转身就走')
        fixes.append(f'行{i+1}: 言临转身就走 -> 我转身就走')
    
    # "言临深吸一口气" -> "我深吸一口气"
    if '言临深吸一口气' in line:
        lines[i] = line.replace('言临深吸一口气', '我深吸一口气')
        fixes.append(f'行{i+1}: 言临深吸一口气 -> 我深吸一口气')
    
    # "言临谢过" -> "我谢过"
    if '言临谢过' in line:
        lines[i] = line.replace('言临谢过', '我谢过')
        fixes.append(f'行{i+1}: 言临谢过 -> 我谢过')
    
    # "言临点开" -> "我点开"
    if '言临点开' in line:
        lines[i] = line.replace('言临点开', '我点开')
        fixes.append(f'行{i+1}: 言临点开 -> 我点开')
    
    # "言临把手机" -> "我把手机"
    if '言临把手机' in line:
        lines[i] = line.replace('言临把手机', '我把手机')
        fixes.append(f'行{i+1}: 言临把手机 -> 我把手机')
    
    # "言临双手" -> "我双手"
    if '言临双手' in line:
        lines[i] = line.replace('言临双手', '我双手')
        fixes.append(f'行{i+1}: 言临双手 -> 我双手')
    
    # "言临绕到" -> "我绕到"
    if '言临绕到' in line:
        lines[i] = line.replace('言临绕到', '我绕到')
        fixes.append(f'行{i+1}: 言临绕到 -> 我绕到')
    
    # "言临站在" -> "我站在"
    if '言临站在' in line:
        lines[i] = line.replace('言临站在', '我站在')
        fixes.append(f'行{i+1}: 言临站在 -> 我站在')
    
    # "言临突然想到" -> "我突然想到"
    if '言临突然想到' in line:
        lines[i] = line.replace('言临突然想到', '我突然想到')
        fixes.append(f'行{i+1}: 言临突然想到 -> 我突然想到')
    
    # "言临想起" -> "我，想起" (特殊处理，避免"我想起"变成第一人称叙述)
    if '言临想起' in line:
        lines[i] = line.replace('言临想起', '我')
        fixes.append(f'行{i+1}: 言临想起 -> 我')
    
    # "这是言临逃离" -> "这是我逃离"
    if '这是言临逃离' in line:
        lines[i] = line.replace('这是言临逃离', '这是我逃离')
        fixes.append(f'行{i+1}: 这是言临逃离 -> 这是我逃离')

# 保存
output = '\n'.join(lines)
with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.8.md', 'w', encoding='utf-8') as f:
    f.write(output)

print(f'\n修复完成，共 {len(fixes)} 处:')
for fix in fixes:
    print(f'  {fix}')

# 再次列出剩余的"言临"
print('\n=== 修复后剩余的"言临" ===')
remaining = []
for i in range(chapter4_start, chapter4_end):
    if '言临' in lines[i]:
        remaining.append((i+1, lines[i].strip()))

print(f'剩余 {len(remaining)} 处:')
for loc, text in remaining[:30]:
    print(f'行{loc}: {text[:80]}')
