import os,base64 
base=r'C:\\project\\aixiaoshuo' 
proj=os.path.join(base,'\u767e\u9b3c\u5165\u57ce') 
outdir=os.path.join(proj,'\u8bc4\u4ef7') 
os.makedirs(outdir,exist_ok=True) 
mapping=[ 
    ('tmp_eval_p1.b64','\u7b2c\u4e00\u90e8_\u7eb8\u5f20\u6b8b\u7559_\u8bc4\u4ef7.md'), 
    ('tmp_eval_p2.b64','\u7b2c\u4e8c\u90e8_\u89e3\u91ca\u5d29\u5854_\u8bc4\u4ef7.md'), 
    ('tmp_eval_p3.b64','\u7b2c\u4e09\u90e8_\u5173\u7cfb\u5d29\u5854_\u8bc4\u4ef7.md'), 
    ('tmp_eval_p4.b64','\u7b2c\u56db\u90e8_\u5408\u4e3a\u4e00\u7ae0_\u8bc4\u4ef7.md'), 
    ('tmp_eval_overall.b64','\u603b\u4f53\u8bc4\u4ef7_\u7ec8\u5ba1\u7248.md'), 
] 
for b64name,outname in mapping: 
    b64path=os.path.join(base,b64name) 
    data=open(b64path,'rb').read() 
    raw=base64.b64decode(data) 
    open(os.path.join(outdir,outname),'wb').write(raw) 
    os.remove(b64path) 
print('ok')
