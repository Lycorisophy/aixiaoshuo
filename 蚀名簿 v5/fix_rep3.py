# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.5.md'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 删除第6239-6251行的重复（索引6238-6250）
# 从"他的手里拿着那个文件夹，手指在轻轻摩挲着边缘。"开始
new_lines = []
removed = 0

for i, line in enumerate(lines):
    # 如果是第6239行（索引6238）开始
    if i == 6238 and '他的手里拿着那个文件夹' in line:
        # 跳过直到"真相。"之后的空行
        j = i
        while j < len(lines):
            if '"真相。"' in lines[j]:
                j += 2  # 跳过"真相。"和下一行空行
                break
            j += 1
        # 删除这些行
        removed = j - i
        i = j - 1
        continue
    new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'删除 {removed} 行')
print(f'当前行数: {len(new_lines)}')
