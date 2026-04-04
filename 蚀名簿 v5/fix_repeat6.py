# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 通过内容匹配删除
# 查找重复的"什么意思？"后跟"出什么事？"
new_lines = []
i = 0
removed = 0
while i < len(lines):
    current = lines[i].strip()
    
    # 如果当前行是"什么意思？"且下一行是空，再下是"出什么事？"
    if current == '"什么意思？"' and i+2 < len(lines):
        next1 = lines[i+1].strip()
        next2 = lines[i+2].strip() if i+2 < len(lines) else ''
        if next1 == '' and next2 == '"出什么事？"':
            # 检查再下一个是否是"失踪。"
            if i+3 < len(lines) and '"失踪。"' in lines[i+3]:
                # 检查再再下一个是否也是空然后又是"什么意思？"
                if i+5 < len(lines) and lines[i+4].strip() == '' and '"什么意思？"' in lines[i+5]:
                    # 这是重复块，跳过第一个重复（保留第一次出现）
                    pass
    
    new_lines.append(lines[i])
    i += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'当前行数: {len(new_lines)}')
