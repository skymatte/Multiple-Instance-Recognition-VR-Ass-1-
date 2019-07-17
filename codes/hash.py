'''def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
'''
import hashlib
def file_as_bytes(file):
    with file:
        return file.read()

print hashlib.md5(file_as_bytes(open("./Final.ipynb", 'rb'))).hexdigest()

