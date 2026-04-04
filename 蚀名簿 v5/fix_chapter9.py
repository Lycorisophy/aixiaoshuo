# -*- coding: utf-8 -*-
"""
《蚀名簿》v8.5 第9-11节对话重复修复脚本
"""

def fix_chapter9_repetition():
    filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.5.md'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_len = len(content)
    
    # 修复第9节的重复对话块
    # 第一次出现
    old1 = '''一下。

两下。

三下。

"你告诉他了？"顾清舟终于开口。

"告诉什么？"

"真相。"

他的手里拿着那个文件夹，手指在轻轻摩挲着边缘。

一下。

两下。

三下。

"你告诉他了？"顾清舟终于开口。

"告诉什么？"

"真相。"'''
    
    new1 = '''一下。

两下。

三下。

"你告诉他了？"顾清舟终于开口。

"告诉什么？"

"真相。"'''
    
    if old1 in content:
        content = content.replace(old1, new1)
        print("已修复第9节对话重复")
    
    # 修复其他重复
    # 词汇重复："显得格外显得格外"
    old2 = "显得格外显得格外……"
    new2 = "显得格外……"
    if old2 in content:
        content = content.replace(old2, new2)
        print("已修复词汇重复：显得格外显得格外")
    
    # 词汇重复："那副那副"
    old3 = "那副那副旧手套"
    new3 = "那副旧手套"
    if old3 in content:
        content = content.replace(old3, new3)
        print("已修复词汇重复：那副那副")
    
    # 词汇重复："一丝一丝"
    old4 = "一丝一丝说不清的情绪"
    new4 = "一丝说不清的情绪"
    if old4 in content:
        content = content.replace(old4, new4)
        print("已修复词汇重复：一丝一丝")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"原始长度: {original_len}")
    print(f"修复后长度: {len(content)}")
    print(f"删除: {original_len - len(content)} 字符")

if __name__ == '__main__':
    fix_chapter9_repetition()
