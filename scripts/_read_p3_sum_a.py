# -*- coding: utf-8 - 
import os 
root=r'C:\\project\\bg' 
pref='\u7b2c\u4e09\u90e8' 
part=None 
for d in os.listdir(root): 
    p=os.path.join(root,d) 
    if os.path.isdir(p) and d.startswith(pref): 
        part=p; break 
assert part 
files=[f for f in os.listdir(part) if f.endswith('_\u6458\u8981.md') or f=='\u6458\u8981.md'] 
files.sort() 
for f in files[:7]: 
    path=os.path.join(part,f) 
    print('\n\n===== '+f+' =====\n') 
    print(open(path,'r',encoding='utf-8').read())
