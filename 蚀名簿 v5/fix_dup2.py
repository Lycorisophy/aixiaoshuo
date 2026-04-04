# -*- coding: utf-8 -*-
filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.5.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 修复对话重复
old = '\n\n他的手里拿着那个文件夹，手指在轻轻摩挲着边缘。\n\n一下。\n\n两下。\n\n三下。\n\n"你告诉他了？"顾清舟终于开口。\n\n"告诉什么？"\n\n"真相。"'
new = ''

count = content.count(old)
if count > 0:
    content = content.replace(old, new)
    print(f'已修复 {count} 处重复')
else:
    print('未找到')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
