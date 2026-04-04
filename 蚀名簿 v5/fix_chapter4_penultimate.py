# -*- coding: utf-8 -*-
"""修复第四章剩余的叙述中的言临"""
with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.8.md', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# 找出第四章范围
start = end = None
for i, line in enumerate(lines):
    if '## 第 25 节' in line:
        start = i
    elif '## 第 33 节' in line:
        end = i
        break

fixes = []
for i in range(start, end):
    line = lines[i]
    original = line
    
    # 需要修复的模式
    if '言临顿了顿' in line:
        line = line.replace('言临顿了顿', '我顿了顿')
        fixes.append(f'行{i+1}: 言临顿了顿 -> 我顿了顿')
    
    if '言临接过' in line:
        line = line.replace('言临接过', '我接过')
        fixes.append(f'行{i+1}: 言临接过 -> 我接过')
    
    if '言临把钥匙' in line:
        line = line.replace('言临把钥匙', '我把钥匙')
        fixes.append(f'行{i+1}: 言临把钥匙 -> 我把钥匙')
    
    if '言临推开门' in line:
        line = line.replace('言临推开门', '我推开门')
        fixes.append(f'行{i+1}: 言临推开门 -> 我推开门')
    
    if '但言临逃了' in line:
        line = line.replace('但言临逃了', '但我逃了')
        fixes.append(f'行{i+1}: 但言临逃了 -> 但我逃了')
    
    if '他走到言临面前' in line:
        line = line.replace('他走到言临面前', '他走到我面前')
        fixes.append(f'行{i+1}: 他走到言临面前 -> 他走到我面前')
    
    if '他用写字告诉言临' in line:
        line = line.replace('他用写字告诉言临', '他用写字告诉我')
        fixes.append(f'行{i+1}: 他用写字告诉言临 -> 他用写字告诉我')
    
    if '言临想不起来' in line:
        line = line.replace('言临想不起来', '我想不起来')
        fixes.append(f'行{i+1}: 言临想不起来 -> 我想不起来')
    
    if '言临接住' in line:
        line = line.replace('言临接住', '我接住')
        fixes.append(f'行{i+1}: 言临接住 -> 我接住')
    
    if '言临接过钥匙' in line:
        line = line.replace('言临接过钥匙', '我接过钥匙')
        fixes.append(f'行{i+1}: 言临接过钥匙 -> 我接过钥匙')
    
    if '言临看着' in line and '言临看着那份' not in line:
        line = line.replace('言临看着', '我看着')
        fixes.append(f'行{i+1}: 言临看着 -> 我看着')
    
    lines[i] = line

# 保存
output = '\n'.join(lines)
with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.8.md', 'w', encoding='utf-8') as f:
    f.write(output)

print(f'修复完成，共 {len(fixes)} 处')
for fix in fixes[:30]:
    print(f'  {fix}')

# 统计剩余
remaining = sum(1 for i in range(start, end) if '言临' in lines[i])
print(f'\n剩余 {remaining} 处"言临"')
