# -*- coding: utf-8 -*-
"""
《蚀名簿》v8.4 精细修复脚本
处理短句重复和连续重复段落
"""

def fix_short_consecutive_duplicates(filepath):
    """
    修复文件中连续的短句重复（如"什么意思？"/"出什么事？"等）
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    changes = []
    i = 0
    
    while i < len(lines) - 1:
        current = lines[i].strip()
        
        # 跳过空行
        if current == '':
            i += 1
            continue
        
        # 查找连续相同的短句（用于对话）
        found_idx = -1
        
        # 对于较短的句子（用于对话），扩大搜索范围
        if 5 <= len(current) <= 50:
            for j in range(i + 1, min(i + 5, len(lines))):
                next_line = lines[j].strip()
                if current == next_line:
                    found_idx = j
                    break
        
        if found_idx > 0:
            changes.append({
                'line': found_idx + 1,
                'content': current
            })
            lines.pop(found_idx)
        else:
            i += 1
    
    # 写入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    return changes, len(lines)

def main():
    output_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
    
    print("开始精细修复（处理对话重复）...")
    
    changes, total = fix_short_consecutive_duplicates(output_file)
    
    print(f"找到并修复 {len(changes)} 处短句重复")
    print(f"当前文件总行数: {total}")
    
    if changes:
        print("\n删除的短句重复:")
        for c in changes[:20]:
            print(f"  第{c['line']}行: {c['content']}")
    
    print("\n处理完成!")

if __name__ == '__main__':
    main()
