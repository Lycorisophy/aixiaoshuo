import os 
base=r'C:\\project\\aixiaoshuo' 
proj=os.path.join(base,'\u767e\u9b3c\u5165\u57ce') 
evaldir=os.path.join(proj,'\u8bc4\u4ef7') 
os.makedirs(evaldir,exist_ok=True) 
print(evaldir)
