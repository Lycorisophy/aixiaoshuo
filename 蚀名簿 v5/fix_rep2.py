# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.5.md'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 删除第6237-6248行的重复（索引6236-6247）
# "他的手里拿着...三下。你告诉他了？..."
new_lines = []
skip_mode = False
skip_count = 0

for i, line in enumerate(lines):
    # 第6237行开始（索引6236）
    if i == 6236 and '他的手里拿着那个文件夹' in line:
        skip_mode = True
        skip_count = 0
    
    if skip_mode:
        skip_count += 1
        # 跳过直到"真相。"之后的第一行
        if '"真相。"' in line:
            skip_mode = False
            skip_count -= 1  # 不计这一行
        continue
    
    new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'删除 {skip_count} 行')
print(f'当前行数: {len(new_lines)}')
