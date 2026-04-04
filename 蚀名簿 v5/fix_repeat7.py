# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 找到需要删除的行
# 第二次出现的"什么意思？"开始，删除到"失踪。"之后
skip_mode = False
skip_count = 0
new_lines = []

for i, line in enumerate(lines):
    if skip_mode:
        skip_count += 1
        if line.strip() == '"失踪。"':
            skip_mode = False
        continue
    
    # 如果遇到第二个"什么意思？"（在"失踪。"之后）
    if line.strip() == '"什么意思？"' and '"失踪。"' in ''.join(lines[max(0,i-20):i]):
        skip_mode = True
        skip_count += 1
        continue
    
    new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'删除 {skip_count} 行')
print(f'当前行数: {len(new_lines)}')
