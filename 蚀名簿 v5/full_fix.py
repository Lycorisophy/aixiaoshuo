# -*- coding: utf-8 -*-
"""
《蚀名簿》v8.5 完整修复脚本
一次性处理第16节省略号问题
"""
import re
import shutil

def fix_spaced_text(text):
    """将"字……字……字……"格式转换为正常句子"""
    lines = text.split('\n')
    result = []
    for line in lines:
        if '……' in line or '…' in line:
            # 检查是否是"字……"格式
            if re.match(r'^[\u4e00-\u9fa5]……', line) or re.search(r'[\u4e00-\u9fa5]……', line):
                fixed = line.replace('……', '').replace('…', '')
                fixed = ' '.join(fixed.split())
                if fixed and not fixed.endswith(('。', '？', '！', '：', '；', '、', '，')):
                    fixed = fixed + '。'
                result.append(fixed)
            else:
                result.append(line)
        else:
            result.append(line)
    return '\n'.join(result)

def main():
    input_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
    output_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.5.md'
    
    # 复制
    shutil.copy(input_file, output_file)
    print("已复制v8.4到v8.5")
    
    # 读取
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到第16节位置
    lines = content.split('\n')
    chapter16_start = None
    chapter17_start = None
    
    for i, line in enumerate(lines):
        if '## 第 16 节' in line:
            chapter16_start = i
        elif '## 第 17 节' in line and chapter16_start:
            chapter17_start = i
            break
    
    if chapter16_start and chapter17_start:
        print(f"第16节: {chapter16_start+1} - {chapter17_start+1}行")
        
        # 统计
        chapter16_text = '\n'.join(lines[chapter16_start:chapter17_start])
        old_count = chapter16_text.count('……') + chapter16_text.count('…')
        print(f"省略号数量: {old_count}")
        
        # 修复
        fixed_text = fix_spaced_text(chapter16_text)
        new_count = fixed_text.count('……') + fixed_text.count('…')
        print(f"修复后: {new_count}")
        
        # 重建
        new_lines = lines[:chapter16_start] + fixed_text.split('\n') + lines[chapter17_start:]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
        print(f"完成！总行数: {len(new_lines)}")
    else:
        print("未找到章节")

if __name__ == '__main__':
    main()
