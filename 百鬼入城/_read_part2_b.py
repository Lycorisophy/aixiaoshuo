import os 
base=r'C:\project\bg' 
part=[d for d in os.listdir(base) if os.path.isdir(os.path.join(base,d)) and d.startswith('\u7b2c\u4e8c\u90e8')][0] 
p=os.path.join(base,part) 
files=sorted([f for f in os.listdir(p) if f.lower().endswith('.md')]) 
sel=files[12:] 
for fn in sel: 
    print('\\n' + '='*20 + ' ' + fn + ' ' + '='*20) 
    print(open(os.path.join(p,fn),encoding='utf-8').read())
