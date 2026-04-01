import os 
root=r'C:\\project\\bg' 
pref='\u7b2c\u4e09\u90e8' 
part=None 
for d in os.listdir(root): 
    p=os.path.join(root,d) 
    if os.path.isdir(p) and d.startswith(pref): 
        part=p 
        break 
assert part, 'part3 not found' 
files=[f for f in os.listdir(part) if f.lower().endswith('.md')] 
files.sort() 
print(part) 
print(len(files)) 
for f in files: 
    print(f)
