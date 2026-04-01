import os 
root=r'C:\\project\\aixiaoshuo' 
target='\u767e\u9b3c\u5165\u57ce' 
proj=os.path.join(root,target) 
print('PROJ',proj) 
print('EXISTS',os.path.isdir(proj)) 
for name in sorted(os.listdir(proj)): 
    print(name)
