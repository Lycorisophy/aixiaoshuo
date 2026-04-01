import os 
base=r'C:\\project\\aixiaoshuo' 
proj=os.path.join(base,'\u767e\u9b3c\u5165\u57ce') 
parts=['\u7b2c\u4e8c\u90e8','\u7b2c\u4e09\u90e8','\u7b2c\u56db\u90e8'] 
for pref in parts: 
    d=None 
    for name in os.listdir(proj): 
        if name.startswith(pref) and os.path.isdir(os.path.join(proj,name)): 
            d=os.path.join(proj,name); break 
    print('\n\n===== '+(os.path.basename(d) if d else pref)+' =====') 
    if not d: 
        print('NOT FOUND'); continue 
    sum_path=os.path.join(d,'\u6458\u8981.md') 
    if os.path.isfile(sum_path): 
        print(open(sum_path,'r',encoding='utf-8').read()) 
    else: 
        print('NO_SUMMARY_MD')
