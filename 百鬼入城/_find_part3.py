import os 
root=r'C:\\project\\bg' 
pref='\u7b2c\u4e09\u90e8' 
for d in os.listdir(root): 
    p=os.path.join(root,d) 
    if os.path.isdir(p) and d.startswith(pref): 
        print(d)
