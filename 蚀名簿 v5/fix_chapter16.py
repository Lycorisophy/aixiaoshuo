# -*- coding: utf-8 -*-
"""
《蚀名簿》v8.5 第16节修复脚本
功能：将"字……字……字……"格式转换为正常句子
"""

import re

def fix_spaced_chinese(text):
    """
    将"字……字……字……"格式转换为正常句子
    例如："我……不……知道。" -> "我不知道。"
    """
    # 匹配模式：汉字后跟省略号
    # 将"字……字……字……"转换为"字字字……"然后再处理
    
    lines = text.split('\n')
    result_lines = []
    
    for line in lines:
        # 检查是否是"字……"格式的行
        if re.match(r'^[\u4e00-\u9fa5]……', line) or '……' in line:
            # 移除所有"……"和"…"并压缩空格
            fixed = line.replace('……', '').replace('…', '')
            fixed = ' '.join(fixed.split())  # 移除多余空格但保留词语边界
            
            # 如果原本是句子，添加标点
            if fixed and not fixed.endswith(('。', '？', '！', '：', '；', '、', '，')):
                fixed = fixed + '。'
            
            result_lines.append(fixed)
        else:
            result_lines.append(line)
    
    return '\n'.join(result_lines)

def process_file():
    input_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
    output_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.5.md'
    
    # 复制文件
    import shutil
    shutil.copy(input_file, output_file)
    print("已复制v8.4到v8.5")
    
    # 读取文件
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到第16节的位置
    lines = content.split('\n')
    
    # 查找第16节开始
    chapter16_start = None
    chapter17_start = None
    
    for i, line in enumerate(lines):
        if '## 第 16 节' in line or '## 第 16节' in line:
            chapter16_start = i
        elif ('## 第 17 节' in line or '## 第 17节' in line) and chapter16_start:
            chapter17_start = i
            break
    
    print(f"第16节开始行: {chapter16_start + 1 if chapter16_start else '未找到'}")
    print(f"第17节开始行: {chapter17_start + 1 if chapter17_start else '未找到'}")
    
    if chapter16_start and chapter17_start:
        # 修复第16节内容
        chapter16_content = '\n'.join(lines[chapter16_start:chapter17_start])
        
        # 统计原始格式
        spaced_count = chapter16_content.count('……') + chapter16_content.count('…')
        print(f"第16节省略号数量: {spaced_count}")
        
        # 修复内容
        fixed_content = fix_spaced_chinese(chapter16_content)
        
        # 统计修复后
        fixed_spaced_count = fixed_content.count('……') + fixed_content.count('…')
        print(f"修复后省略号数量: {fixed_spaced_count}")
        
        # 重建文件
        fixed_lines = fixed_content.split('\n')
        new_lines = lines[:chapter16_start] + fixed_lines + lines[chapter17_start:]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
        print(f"v8.5生成完成")
        print(f"总行数: {len(new_lines)}")
    else:
        print("未找到第16节")

if __name__ == '__main__':
    process_file()
