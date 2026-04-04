# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.5.md'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 删除第6239-6251行的重复
new_lines = []
i = 0
while i < len(lines):
    if i == 6238 and '他的手里拿着' in lines[i]:
        # 跳过直到找到'真相。'
        while i < len(lines) and '真相' not in lines[i]:
            i += 1
        i += 1  # 跳过'真相。'
        if i < len(lines) and lines[i].strip() == '':
            i += 1
    else:
        new_lines.append(lines[i])
        i += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'删除: {len(lines) - len(new_lines)}行')
