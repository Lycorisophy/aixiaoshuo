# -*- coding: utf-8 -*-
"""
《蚀名簿》v8.4 重复内容全面扫描脚本 v2
更低的阈值，更严格的检测
"""

def scan_duplicates_v2(filepath, min_len=10, max_gap=5):
    """
    全面扫描文件中的重复内容
    min_len: 最小重复字符数（降低到10）
    max_gap: 最大间隔行数（缩小到5）
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    duplicates = []
    
    for i in range(len(lines) - 1):
        current = lines[i].strip()
        
        # 跳过空行和标记行
        if current == '' or current.startswith('##') or current.startswith('---') or current.startswith('# '):
            continue
        
        # 在指定范围内查找完全相同的内容
        for j in range(i + 1, min(i + 1 + max_gap, len(lines))):
            next_line = lines[j].strip()
                
            if current == next_line and len(current) >= min_len:
                duplicates.append({
                    'first_line': i + 1,
                    'dup_line': j + 1,
                    'gap': j - i,
                    'content': current[:80] + '...' if len(current) > 80 else current,
                    'len': len(current)
                })
                break
    
    return duplicates

def main():
    output_file = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
    
    print("开始全面扫描v8.4重复内容（严格模式）...")
    
    duplicates = scan_duplicates_v2(output_file, min_len=10, max_gap=5)
    
    print(f"\n发现 {len(duplicates)} 处重复\n")
    
    if duplicates:
        print("重复内容列表：")
        for i, d in enumerate(duplicates[:50], 1):  # 只显示前50个
            print(f"{i}. 第{d['first_line']}行 和 第{d['dup_line']}行 (间隔{d['gap']}行)")
            print(f"   内容: {d['content']}")
            print()
    
    if len(duplicates) > 50:
        print(f"... 还有 {len(duplicates) - 50} 处未显示")

if __name__ == '__main__':
    main()
