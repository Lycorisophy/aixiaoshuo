# -*- coding: utf-8 -*-
f=open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.8.md','r',encoding='utf-8')
lines=f.readlines()
f.close()

start=end=None
for i,l in enumerate(lines):
    if '## 第 25 节' in l: start=i
    elif '## 第 33 节' in l: end=i; break

count=0
for i in range(start,end):
    # 处理单独的"言临。"或"言临？"
    s=lines[i].strip()
    if s=='"言临。"' or s=='言临。':
        lines[i]=lines[i].replace('言临。','我。'); count+=1
    if s=='"言临。"' or s=='言临。':
        lines[i]=lines[i].replace('"言临。"','"我。"'); count+=1
    if s=='言临？' or s=='"言临？"':
        lines[i]=lines[i].replace('言临？','我？'); count+=1

with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.8.md','w',encoding='utf-8') as f:
    f.writelines(lines)
print(f'修复{count}处')
remaining=sum(1 for i in range(start,end) if '言临' in lines[i])
print(f'剩余{remaining}处')
