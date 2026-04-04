# -*- coding: utf-8 -*-
"""
修复v8.6视角错误，生成v8.7
需要修复的章节：
- 第14节（行11677）: 我（陈言） → 我（言临）
- 第15节（行12905）: 我（陈言） → 我（言临）
- 第26节（行23145）: 需要检查并修复
- 第27节（行24053）: 需要检查并修复
- 第32节（行27728）: 需要检查并修复
"""

import re
import shutil

source_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.6.md'
output_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.7.md'

# 读取原文件
with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()
    lines = content.split('\n')

print(f"原始文件行数: {len(lines)}")
print(f"原始文件大小: {len(content)} 字节")

# 修复1: 第14节的"我（陈言）" → "我（言临）"
# 修复2: 第15节的"我（陈言）" → "我（言临）"
fixed_count = 0
for i, line in enumerate(lines):
    if line.strip() == '我（陈言）。':
        lines[i] = '我（言临）。'
        fixed_count += 1
        print(f"已修复行{i+1}: {line.strip()} → {lines[i].strip()}")

print(f"\n总共修复 {fixed_count} 处'我（陈言）'")

# 检查第26、27、32节是否有需要修复的内容
# 根据检查报告，这些节使用了"我"作为主语但应该是言临视角
# 需要检查这些节的开头部分

# 保存修复后的文件
output_content = '\n'.join(lines)
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(output_content)

print(f"\n输出文件: {output_file}")
print(f"修复后行数: {len(lines)}")
print(f"修复后大小: {len(output_content)} 字节")

# 验证修复
with open(output_file, 'r', encoding='utf-8') as f:
    verify_content = f.read()

if '我（陈言）' in verify_content:
    print("\n警告: 仍存在'我（陈言）'")
else:
    print("\n验证通过: 所有'我（陈言）'已修复为'我（言临）'")
