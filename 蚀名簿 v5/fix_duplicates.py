# -*- coding: utf-8 -*-
"""
《蚀名簿》v8.3 重复段落修复脚本
功能：检测并删除连续重复的段落
"""

import re

def read_file(filepath):
    """读取文件内容"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()

def find_consecutive_duplicates(lines, min_duplicate_chars=50, max_gap=5):
    """
    查找连续重复的段落
    min_duplicate_chars: 最小重复字符数
    max_gap: 允许的最大间隔行数
    """
    duplicates = []
    
    for i in range(len(lines) - 1):
        # 跳过空行
        if lines[i].strip() == '':
            continue
            
        # 比较后续行是否有相同内容
        for j in range(i + 1, min(i + 1 + max_gap, len(lines))):
            if lines[j].strip() == lines[i].strip() and len(lines[i].strip()) >= min_duplicate_chars:
                # 检查i和j之间是否有实质性内容变化
                between_content = ''.join(lines[i+1:j])
                if between_content.strip() == '':
                    duplicates.append((i, j, lines[i].strip()[:50]))
                    break
    
    return duplicates

def fix_duplicates_in_range(filepath, start_line, end_line, output_path):
    """
    修复指定范围内的重复段落
    start_line: 起始行（1-indexed）
    end_line: 结束行（1-indexed）
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 转换为0-indexed
    start_idx = start_line - 1
    end_idx = end_line
    
    changes = []
    i = start_idx
    
    while i < end_idx and i < len(lines) - 1:
        # 跳过空行
        if lines[i].strip() == '':
            i += 1
            continue
            
        current_line = lines[i].strip()
        
        # 在小范围内查找重复（max_gap = 10行）
        found_duplicate = False
        for j in range(i + 1, min(i + 11, end_idx, len(lines))):
            next_line = lines[j].strip()
            
            # 如果找到完全相同且足够长的内容
            if current_line == next_line and len(current_line) >= 30:
                changes.append({
                    'type': 'delete',
                    'line': j + 1,  # 1-indexed
                    'content': next_line[:60] + '...'
                })
                # 删除重复行
                lines.pop(j)
                found_duplicate = True
                end_idx -= 1  # 调整结束索引
                # 不增加i，因为可能有更多重复
                break
        
        if not found_duplicate:
            i += 1
    
    # 写入输出文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    return changes, len(lines)

def main():
    input_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.3.md'
    output_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
    
    print("开始修复《蚀名簿》v8.3...")
    
    # 先复制原文件
    import shutil
    shutil.copy(input_file, output_file)
    print(f"已复制原文件到 v8.4")
    
    # 处理第1-500行
    print("\n处理第1-500行...")
    changes, total_lines = fix_duplicates_in_range(
        output_file, 
        start_line=1, 
        end_line=500, 
        output_path=output_file
    )
    
    print(f"找到并修复 {len(changes)} 处重复")
    for c in changes[:20]:  # 只显示前20个
        print(f"  删除第{c['line']}行: {c['content']}")
    
    print(f"\n当前文件总行数: {total_lines}")
    print("处理完成!")

if __name__ == '__main__':
    main()
