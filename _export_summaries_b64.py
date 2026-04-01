import os,base64 
base=r'C:\\project\\aixiaoshuo' 
proj=os.path.join(base,'\u767e\u9b3c\u5165\u57ce') 
prefs=['\u7b2c\u4e00\u90e8','\u7b2c\u4e8c\u90e8','\u7b2c\u4e09\u90e8','\u7b2c\u56db\u90e8'] 
for pref in prefs: 
    part=None 
    for name in os.listdir(proj): 
        if name.startswith(pref) and os.path.isdir(os.path.join(proj,name)): 
            part=os.path.join(proj,name); break 
    print('@@PART',pref, os.path.basename(part) if part else 'NOT_FOUND') 
    if not part: 
        continue 
    cand=[] 
    p=os.path.join(part,'\u6458\u8981.md') 
    if os.path.isfile(p): 
        cand=[p] 
    else: 
        for fn in os.listdir(part): 
            if fn.endswith('_\u6458\u8981.md') or fn.endswith('_\u6458\u8981.txt'): 
                cand.append(os.path.join(part,fn)) 
        cand.sort() 
    for fp in cand: 
        data=open(fp,'rb').read() 
        b64=base64.b64encode(data).decode('ascii') 
        print('@@FILE',os.path.basename(fp),len(data)) 
        print(b64)
