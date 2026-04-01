import os 
base=r'C:\\project\\aixiaoshuo' 
proj=os.path.join(base,'\u767e\u9b3c\u5165\u57ce') 
parts=[] 
for d in os.listdir(proj): 
    p=os.path.join(proj,d) 
    if os.path.isdir(p) and (d.startswith('\u7b2c\u4e00\u90e8') or d.startswith('\u7b2c\u4e8c\u90e8') or d.startswith('\u7b2c\u4e09\u90e8') or d.startswith('\u7b2c\u56db\u90e8')): 
        parts.append(d) 
for d in sorted(parts): 
    print(d)
