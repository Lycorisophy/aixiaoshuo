# -*- coding: utf-8 -*-
"""
《蚀名簿》v8.4 全文件重复清理脚本
处理全文件中所有连续重复的段落
"""

def fix_all_duplicates(filepath, min_len=15, max_gap=8):
    """
    修复文件中所有连续重复的段落
    min_len: 最小重复字符数
    max_gap: 最大间隔行数
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changes = []
    i = 0
    total_removed = 0
    
    while i < len(lines) - 1:
        current = lines[i].strip()
        
        # 跳过空行和标记行
        if current == '' or current.startswith('##') or current.startswith('---') or current.startswith('# '):
            i += 1
            continue
        
        # 在指定范围内查找完全相同的内容
        found_idx = -1
        for j in range(i + 1, min(i + 1 + max_gap, len(lines))):
            next_line = lines[j].strip()
            # 对话类短句（5-40字）更容易重复，阈值较低
            if min_len <= len(current) <= 40:
                threshold = min_len
            else:
                threshold = min_len
                
            if current == next_line and len(current) >= threshold:
                found_idx = j
                break
        
        if found_idx > 0:
            changes.append({
                'line': found_idx + 1,
                'content': current[:60] + '...' if len(current) > 60 else current
            })
            lines.pop(found_idx)
            total_removed += 1
        else:
            i += 1
    
    # 写入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    return changes, total_removed, len(lines)

def main():
    output_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
    
    print("开始全文件重复清理...")
    
    # 多次运行直到没有新发现
    total_changes = 0
    for round_num in range(1, 6):  # 最多5轮
        changes, removed, total = fix_all_duplicates(output_file)
        if removed == 0:
            print(f"第{round_num}轮：无新发现")
            break
        print(f"第{round_num}轮：删除 {removed} 处重复")
        total_changes += removed
        if round_num == 1:
            for c in changes[:15]:
                print(f"  第{c['line']}行: {c['content']}")
    
    print(f"\n总计删除: {total_changes} 处重复")
    print(f"当前文件总行数: {total}")
    print("处理完成!")

if __name__ == '__main__':
    main()
