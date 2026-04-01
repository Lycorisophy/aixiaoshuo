import base64, pathlib
b=pathlib.Path(r'C:\project\bg\_tmp_read2.b64').read_bytes()
pathlib.Path(r'C:\project\bg\_tmp_read2.py').write_bytes(base64.b64decode(b))
