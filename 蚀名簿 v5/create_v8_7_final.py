# -*- coding: utf-8 -*-
"""从v8.6重新创建v8.7，一次性修复所有视角错误"""

import shutil

# 先复制v8.6为v8.7
source = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.6.md'
dest = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.7.md'
shutil.copy2(source, dest)
print(f'已复制 {source} -> {dest}')

# 读取v8.7
with open(dest, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print(f'原始行数: {len(lines)}')

fixes = []

# 第14节: 我（陈言）。 -> 我（言临）。
for i, line in enumerate(lines):
    if line.strip() == '我（陈言）。':
        lines[i] = '我（言临）。'
        fixes.append(f'行{i+1}: 第14节修复')

# 第15节: 我（陈言）。 -> 我（言临）。
for i, line in enumerate(lines):
    if line.strip() == '我（陈言）。':
        lines[i] = '我（言临）。'
        fixes.append(f'行{i+1}: 第15节修复')

# 第27节修复
for i, line in enumerate(lines):
    if '我一直以为' in line and '井底' in line:
        lines[i] = line.replace('我一直以为', '言临一直以为')
        fixes.append(f'行{i+1}: 第27节 - 我一直以为')
    if '直到那天我才明白' in line:
        lines[i] = line.replace('直到那天我才明白', '直到那天言临才明白')
        fixes.append(f'行{i+1}: 第27节 - 直到那天我才明白')
    if '我心里一沉' in line:
        lines[i] = line.replace('我心里一沉', '言临心里一沉')
        fixes.append(f'行{i+1}: 第27节 - 我心里一沉')
    if '这意味着' in line and '紫印链' in line:
        lines[i] = line.replace('这意味着', '言临意识到这意味着')
        fixes.append(f'行{i+1}: 第27节 - 这意味着')
    if '我们沿着' in line and '材料室' in line:
        lines[i] = line.replace('我们沿着', '他们沿着')
        fixes.append(f'行{i+1}: 第27节 - 我们沿着')
    if '我用指尖沾了一点' in line:
        lines[i] = line.replace('我用指尖沾了一点', '言临用指尖沾了一点')
        fixes.append(f'行{i+1}: 第27节 - 我用指尖')

# 第32节修复
for i, line in enumerate(lines):
    if '我把手机递过去' in line:
        lines[i] = line.replace('我把手机递过去', '言临把手机递过去')
        fixes.append(f'行{i+1}: 第32节 - 我把手机递过去')
    if '他把屏幕递回给我' in line:
        lines[i] = line.replace('他把屏幕递回给我', '他把屏幕递回给言临')
        fixes.append(f'行{i+1}: 第32节 - 屏幕递回给我')
    if '他给了我一套' in line:
        lines[i] = line.replace('他给了我一套', '他给了言临一套')
        fixes.append(f'行{i+1}: 第32节 - 他给了我一套')
    if '我看着那份清单' in line:
        lines[i] = line.replace('我看着那份清单', '言临看着那份清单')
        fixes.append(f'行{i+1}: 第32节 - 我看着那份清单')
    if '不是我脑子里剩下多少' in line:
        lines[i] = line.replace('不是我脑子里剩下多少', '不是言临脑子里剩下多少')
        fixes.append(f'行{i+1}: 第32节 - 不是我脑子里')
    if '是我手里还能剩下多少纸' in line:
        lines[i] = line.replace('是我手里还能剩下多少纸', '是言临手里还能剩下多少纸')
        fixes.append(f'行{i+1}: 第32节 - 是我手里')

# 保存
output = '\n'.join(lines)
with open(dest, 'w', encoding='utf-8') as f:
    f.write(output)

print(f'\n修复完成，共 {len(fixes)} 处:')
for fix in fixes:
    print(f'  {fix}')

print(f'\n输出文件: {dest}')
print(f'修复后行数: {len(lines)}')
