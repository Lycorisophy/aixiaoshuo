# -*- coding: utf-8 -*-
"""
修复v8.7第四章(第25-32节)视角为标准第一人称
方案A：将所有"言临"替换为"我"，使第四章统一为言临的第一人称视角
"""

import shutil

# 先复制v8.7为v8.8
source = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.7.md'
dest = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.8.md'
shutil.copy2(source, dest)
print(f'已复制 v8.7 -> v8.8')

with open(dest, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print(f'原始行数: {len(lines)}')

# 找出第四章的起始和结束位置
chapter4_start = None
chapter4_end = None
chapter5_start = None

for i, line in enumerate(lines):
    if '## 第 25 节' in line:
        chapter4_start = i
        print(f'第四章开始: 行{i+1}')
    elif '## 第 33 节' in line:
        chapter5_start = i
        chapter4_end = i
        print(f'第四章结束: 行{i}')
        print(f'第五章开始: 行{i+1}')
        break

if chapter4_start is None:
    print('错误：未找到第四章开始')
    exit(1)

if chapter4_end is None:
    chapter4_end = len(lines)

# 统计和修复
fixes = []
for i in range(chapter4_start, chapter4_end):
    line = lines[i]
    
    # 需要修复的模式（在第四章范围内的"言临"）
    # 注意：对话中的角色名如"他说"不需要改
    
    # 1. "言临点点头" -> "我点点头"
    if '言临点点头' in line:
        lines[i] = line.replace('言临点点头', '我点点头')
        fixes.append(f'行{i+1}: 言临点点头 -> 我点点头')
    
    # 2. "言临转过身" -> "我转过身"
    if '言临转过身' in line:
        lines[i] = line.replace('言临转过身', '我转过身')
        fixes.append(f'行{i+1}: 言临转过身 -> 我转过身')
    
    # 3. "言临站在人群中" -> "我站在人群中"
    if '言临站在人群中' in line:
        lines[i] = line.replace('言临站在人群中', '我站在人群中')
        fixes.append(f'行{i+1}: 言临站在人群中 -> 我站在人群中')
    
    # 4. "言临盯着" -> "我盯着"
    if '言临盯着' in line:
        lines[i] = line.replace('言临盯着', '我盯着')
        fixes.append(f'行{i+1}: 言临盯着 -> 我盯着')
    
    # 5. "言临一直以为" -> "我一直以为"
    if '言临一直以为' in line:
        lines[i] = line.replace('言临一直以为', '我一直以为')
        fixes.append(f'行{i+1}: 言临一直以为 -> 我一直以为')
    
    # 6. "直到那天言临才明白" -> "直到那天我才明白"
    if '直到那天言临才明白' in line:
        lines[i] = line.replace('直到那天言临才明白', '直到那天我才明白')
        fixes.append(f'行{i+1}: 直到那天言临才明白 -> 直到那天我才明白')
    
    # 7. "言临心里一沉" -> "我心里一沉"
    if '言临心里一沉' in line:
        lines[i] = line.replace('言临心里一沉', '我心里一沉')
        fixes.append(f'行{i+1}: 言临心里一沉 -> 我心里一沉')
    
    # 8. "言临意识到" -> "我意识到"
    if '言临意识到' in line:
        lines[i] = line.replace('言临意识到', '我意识到')
        fixes.append(f'行{i+1}: 言临意识到 -> 我意识到')
    
    # 9. "言临用指尖" -> "我用指尖"
    if '言临用指尖' in line:
        lines[i] = line.replace('言临用指尖', '我用指尖')
        fixes.append(f'行{i+1}: 言临用指尖 -> 我用指尖')
    
    # 10. "言临把手机递过去" -> "我把手机递过去"
    if '言临把手机递过去' in line:
        lines[i] = line.replace('言临把手机递过去', '我把手机递过去')
        fixes.append(f'行{i+1}: 言临把手机递过去 -> 我把手机递过去')
    
    # 11. "他把屏幕递回给言临" -> "他把屏幕递回给我"
    if '他把屏幕递回给言临' in line:
        lines[i] = line.replace('他把屏幕递回给言临', '他把屏幕递回给我')
        fixes.append(f'行{i+1}: 他把屏幕递回给言临 -> 他把屏幕递回给我')
    
    # 12. "他给了言临一套" -> "他给了我一套"
    if '他给了言临一套' in line:
        lines[i] = line.replace('他给了言临一套', '他给了我一套')
        fixes.append(f'行{i+1}: 他给了言临一套 -> 他给了我一套')
    
    # 13. "言临看着那份清单" -> "我看着那份清单"
    if '言临看着那份清单' in line:
        lines[i] = line.replace('言临看着那份清单', '我看着那份清单')
        fixes.append(f'行{i+1}: 言临看着那份清单 -> 我看着那份清单')
    
    # 14. "不是言临脑子里" -> "不是我脑子里"
    if '不是言临脑子里' in line:
        lines[i] = line.replace('不是言临脑子里', '不是我脑子里')
        fixes.append(f'行{i+1}: 不是言临脑子里 -> 不是我脑子里')
    
    # 15. "是言临手里还能剩下多少纸" -> "是我手里还能剩下多少纸"
    if '是言临手里还能剩下多少纸' in line:
        lines[i] = line.replace('是言临手里还能剩下多少纸', '是我手里还能剩下多少纸')
        fixes.append(f'行{i+1}: 是言临手里 -> 是我手里')

# 保存
output = '\n'.join(lines)
with open(dest, 'w', encoding='utf-8') as f:
    f.write(output)

print(f'\n修复完成，共 {len(fixes)} 处:')
for fix in fixes:
    print(f'  {fix}')

print(f'\n输出文件: {dest}')
