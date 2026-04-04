# -*- coding: utf-8 -*-
"""
《蚀名簿》v8.4 重复段落修复脚本 v2
功能：更彻底地检测并删除连续重复的段落
"""

import re

def fix_consecutive_duplicates(filepath):
    """
    修复文件中的连续重复段落
    更激进地检测重复
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changes = []
    i = 0
    removed_count = 0
    
    while i < len(lines) - 1:
        current = lines[i].strip()
        
        # 跳过空行和标记行
        if current == '' or current.startswith('##') or current.startswith('---') or current.startswith('**'):
            i += 1
            continue
        
        # 查找下一个完全相同的内容
        found_idx = -1
        for j in range(i + 1, min(i + 20, len(lines))):
            next_line = lines[j].strip()
            if current == next_line and len(current) >= 20:
                found_idx = j
                break
        
        if found_idx > 0:
            # 删除重复行
            line_num = i + 1
            content_preview = current[:50] + '...' if len(current) > 50 else current
            changes.append({
                'type': 'delete',
                'line': found_idx + 1,
                'content': content_preview
            })
            lines.pop(found_idx)
            removed_count += 1
            # 不增加i，继续检查是否有更多重复
        else:
            i += 1
    
    # 写入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    return changes, removed_count, len(lines)

def main():
    output_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
    
    print("开始第二轮修复...")
    
    # 处理整个文件
    changes, removed, total = fix_consecutive_duplicates(output_file)
    
    print(f"找到并修复 {len(changes)} 处重复")
    print(f"总共删除 {removed} 行")
    print(f"当前文件总行数: {total}")
    
    if changes:
        print("\n删除的重复行:")
        for c in changes[:30]:
            print(f"  第{c['line']}行: {c['content']}")
    
    print("\n处理完成!")

if __name__ == '__main__':
    main()
