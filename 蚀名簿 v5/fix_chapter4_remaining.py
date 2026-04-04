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

# 先列出所有包含"言临"的行
print('\n=== 第四章中包含"言临"的行 ===')
yanlin_lines = []
for i in range(chapter4_start, chapter4_end):
    if '言临' in lines[i]:
        yanlin_lines.append((i+1, lines[i].strip()))

print(f'共发现 {len(yanlin_lines)} 处"言临"')
for loc, text in yanlin_lines[:50]:
    print(f'行{loc}: {text[:80]}')

# 修复所有"言临"为"我"
fixes = []
for i in range(chapter4_start, chapter4_end):
    line = lines[i]
    
    # 跳过对话中需要保留"言临"的部分
    # 例如角色名、他说"言临"等
    
    # "这是言临离开" -> "这是我离开"
    if '这是言临离开' in line:
        lines[i] = line.replace('这是言临离开', '这是我离开')
        fixes.append(f'行{i+1}: 这是言临离开 -> 这是我离开')
    
    # "言临看着" -> "我看着"
    if '言临看着' in line:
        lines[i] = line.replace('言临看着', '我看着')
        fixes.append(f'行{i+1}: 言临看着 -> 我看着')
    
    # "言临没有" -> "我没有"
    if '言临没有' in line:
        lines[i] = line.replace('言临没有', '我没有')
        fixes.append(f'行{i+1}: 言临没有 -> 我没有')
    
    # "言临说" -> "我说"
    if '言临说' in line:
        lines[i] = line.replace('言临说', '我说')
        fixes.append(f'行{i+1}: 言临说 -> 我说')
    
    # "言临问" -> "我问"
    if '言临问' in line:
        lines[i] = line.replace('言临问', '我问')
        fixes.append(f'行{i+1}: 言临问 -> 我问')
    
    # "言临回答" -> "我回答"
    if '言临回答' in line:
        lines[i] = line.replace('言临回答', '我回答')
        fixes.append(f'行{i+1}: 言临回答 -> 我回答')
    
    # "言临点头" -> "我点头"
    if '言临点头' in line:
        lines[i] = line.replace('言临点头', '我点头')
        fixes.append(f'行{i+1}: 言临点头 -> 我点头')
    
    # "言临摇了摇" -> "我摇了摇头"
    if '言临摇了摇' in line:
        lines[i] = line.replace('言临摇了摇', '我摇了摇头')
        fixes.append(f'行{i+1}: 言临摇了摇 -> 我摇了摇头')
    
    # "言临伸出手" -> "我伸出手"
    if '言临伸出手' in line:
        lines[i] = line.replace('言临伸出手', '我伸出手')
        fixes.append(f'行{i+1}: 言临伸出手 -> 我伸出手')
    
    # "言临把手伸" -> "我把手伸"
    if '言临把手伸' in line:
        lines[i] = line.replace('言临把手伸', '我把手伸')
        fixes.append(f'行{i+1}: 言临把手伸 -> 我把手伸')
    
    # "言临坐在" -> "我坐在"
    if '言临坐在' in line:
        lines[i] = line.replace('言临坐在', '我坐在')
        fixes.append(f'行{i+1}: 言临坐在 -> 我坐在')
    
    # "言临感觉" -> "我感觉到"
    if '言临感觉' in line:
        lines[i] = line.replace('言临感觉', '我感觉到')
        fixes.append(f'行{i+1}: 言临感觉 -> 我感觉到')
    
    # "言临抬起" -> "我抬起"
    if '言临抬起' in line:
        lines[i] = line.replace('言临抬起', '我抬起')
        fixes.append(f'行{i+1}: 言临抬起 -> 我抬起')
    
    # "言临低" -> "我低"
    if '言临低头' in line:
        lines[i] = line.replace('言临低头', '我低头')
        fixes.append(f'行{i+1}: 言临低头 -> 我低头')
    
    # "言临忽然" -> "我忽然"
    if '言临忽然' in line:
        lines[i] = line.replace('言临忽然', '我忽然')
        fixes.append(f'行{i+1}: 言临忽然 -> 我忽然')
    
    # "言临慢慢" -> "我慢慢"
    if '言临慢慢' in line:
        lines[i] = line.replace('言临慢慢', '我慢慢')
        fixes.append(f'行{i+1}: 言临慢慢 -> 我慢慢')
    
    # "言临沉默" -> "我沉默"
    if '言临沉默' in line:
        lines[i] = line.replace('言临沉默', '我沉默')
        fixes.append(f'行{i+1}: 言临沉默 -> 我沉默')
    
    # "言临摇头" -> "我摇头"
    if '言临摇头' in line:
        lines[i] = line.replace('言临摇头', '我摇头')
        fixes.append(f'行{i+1}: 言临摇头 -> 我摇头')
    
    # "言临伸出手" -> "我伸出手"
    if '言临伸出手' in line:
        lines[i] = line.replace('言临伸出手', '我伸出手')
        fixes.append(f'行{i+1}: 言临伸出手 -> 我伸出手')
    
    # "言临站" -> "我站"
    if line.strip().startswith('言临站') and '言临站在人群中' not in line:
        lines[i] = line.replace('言临站', '我站')
        fixes.append(f'行{i+1}: 言临站 -> 我站')

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
