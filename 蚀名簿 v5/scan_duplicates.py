# -*- coding: utf-8 -*-
"""
《蚀名簿》v8.4 重复内容全面扫描脚本
"""

def scan_duplicates(filepath, min_len=20, max_gap=15):
    """
    全面扫描文件中的重复内容
    min_len: 最小重复字符数
    max_gap: 最大间隔行数
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
            # 对话类短句阈值较低
            if min_len <= len(current) <= 50:
                threshold = min_len
            else:
                threshold = min_len
                
            if current == next_line and len(current) >= threshold:
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
    
    print("开始全面扫描v8.4重复内容...")
    
    duplicates = scan_duplicates(output_file)
    
    print(f"\n发现 {len(duplicates)} 处重复\n")
    
    if duplicates:
        print("重复内容列表：")
        for i, d in enumerate(duplicates, 1):
            print(f"{i}. 第{d['first_line']}行 和 第{d['dup_line']}行 (间隔{d['gap']}行)")
            print(f"   内容: {d['content']}")
            print(f"   长度: {d['len']}字符")
            print()
    
    # 按位置分组统计
    sections = {}
    for d in duplicates:
        # 估算章节位置（每章约2000行）
        chapter = (d['first_line'] - 1) // 2000 + 1
        if chapter not in sections:
            sections[chapter] = 0
        sections[chapter] += 1
    
    print("\n按章节分布：")
    for chapter in sorted(sections.keys()):
        print(f"  第{chapter}章附近: {sections[chapter]}处")

if __name__ == '__main__':
    main()
