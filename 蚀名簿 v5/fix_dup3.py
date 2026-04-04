# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.5.md'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 删除第6238-6251行的重复（索引6237-6250）
# 从空行开始到"真相。"结束
new_lines = []
skip_start = None

for i, line in enumerate(lines):
    # 检测到第二次出现的"他的手里拿着"时开始跳过
    if '他的手里拿着那个文件夹，手指在轻轻摩挲着边缘。' in line and i > 6000:
        skip_start = i - 1  # 从空行开始
        continue
    
    if skip_start is not None:
        if '"真相。"' in line:
            skip_start = None
        continue
    
    new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'原始行数: {len(lines)}')
print(f'新行数: {len(new_lines)}')
print(f'删除: {len(lines) - len(new_lines)} 行')
