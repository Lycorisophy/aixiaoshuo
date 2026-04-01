import os,base64 
root=r'C:\\project\\bg' 
# decode eval 
eval_b64=open(os.path.join(root,'tmp_p3_eval.b64'),'rb').read() 
eval_name='\u7b2c\u4e09\u90e8_\u5173\u7cfb\u5d29\u5854_\u8bc4\u4ef7.md' 
open(os.path.join(root,eval_name),'wb').write(base64.b64decode(eval_b64)) 
# append overall 
app_b64=open(os.path.join(root,'tmp_p3_overall_append.b64'),'rb').read() 
app=base64.b64decode(app_b64).decode('utf-8') 
with open(os.path.join(root,'\u603b\u4f53\u8bc4\u4ef7.md'),'a',encoding='utf-8') as f: 
    f.write(app) 
# cleanup 
os.remove(os.path.join(root,'tmp_p3_eval.b64')) 
os.remove(os.path.join(root,'tmp_p3_overall_append.b64')) 
print('ok')
