# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 删除第249-253行的重复块（索引248-252）
# "什么意思？" + 空行 + "出什么事？"
new_lines = []
i = 0
removed = 0
while i < len(lines):
    # 如果是第249行（索引248）
    if i == 248 and '什么意思？' in lines[i]:
        # 跳过这一行和下一个空行及"出什么事？"
        removed += 1
        i += 1
        while i < len(lines) and lines[i].strip() == '':
            removed += 1
            i += 1
        if i < len(lines) and '出什么事？' in lines[i]:
            removed += 1
            i += 1
        continue
    new_lines.append(lines[i])
    i += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'删除 {removed} 行')
print(f'当前行数: {len(new_lines)}')
