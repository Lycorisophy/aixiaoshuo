# -*- coding: utf-8 -*-
# 删除最后一处重复

def main():
    filepath = r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.4.md'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 查找第211行附近的重复
    target = "你小时候住这附近？"
    removed = []
    
    new_lines = []
    skip_next = False
    
    for i, line in enumerate(lines):
        if skip_next:
            skip_next = False
            removed.append((i+1, line.strip()))
            continue
            
        stripped = line.strip()
        
        # 检查是否是目标行且下一个是空行
        if stripped == target:
            # 检查是否已经在删除列表中
            if i+1 not in [r[0] for r in removed]:
                skip_next = True
                new_lines.append(line)
                continue
        
        new_lines.append(line)
    
    # 写入
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"删除了 {len(removed)} 行重复")
    for r in removed:
        print(f"  第{r[0]}行: {r[1]}")
    print(f"当前行数: {len(new_lines)}")

if __name__ == '__main__':
    main()
