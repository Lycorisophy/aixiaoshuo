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
    if '败者是言临' in lines[i]:
        lines[i]=lines[i].replace('败者是言临','败者是我'); count+=1
    if '言临这个身份' in lines[i]:
        lines[i]=lines[i].replace('言临这个身份','我的这个身份'); count+=1
    if '如果言临这个身份' in lines[i]:
        lines[i]=lines[i].replace('如果言临这个身份','如果我的这个身份'); count+=1
    if '他看向言临' in lines[i]:
        lines[i]=lines[i].replace('他看向言临','他看向我'); count+=1
    if '你是言临' in lines[i]:
        lines[i]=lines[i].replace('你是言临','你是我'); count+=1
    if '他是言临' in lines[i]:
        lines[i]=lines[i].replace('他是言临','他是我'); count+=1
    if '两个言临——' in lines[i]:
        lines[i]=lines[i].replace('两个言临——','两个人——'); count+=1

with open(r'C:\project\aixiaoshuo\蚀名簿 v5\《蚀名簿》v8.8.md','w',encoding='utf-8') as f:
    f.writelines(lines)
print(f'修复{count}处')
remaining=sum(1 for i in range(start,end) if '言临' in lines[i])
print(f'剩余{remaining}处')
