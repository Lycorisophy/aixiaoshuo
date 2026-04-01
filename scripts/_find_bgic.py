import os 
root=r'C:\\project\\aixiaoshuo' 
target='\u767e\u9b3c\u5165\u57ce' 
p=None 
for d in os.listdir(root): 
    if d==target: 
        p=os.path.join(root,d) 
        break 
print(p or '')
