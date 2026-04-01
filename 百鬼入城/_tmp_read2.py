import os, ctypes
base=r"C:\project\bg"
part=None
for name in os.listdir(base):
    p=os.path.join(base,name)
    if os.path.isdir(p) and name.startswith("第二部"):
        part=p
        break
print("FOUND", part)
GetShortPathNameW=ctypes.windll.kernel32.GetShortPathNameW
buf=ctypes.create_unicode_buffer(260)
GetShortPathNameW(part, buf, 260)
print("SHORT", buf.value)
files=sorted([fn for fn in os.listdir(part) if fn.lower().endswith(".md")])
print("FILES", len(files))
for fn in files:
    print(fn)
