import hashlib

def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    encodeStr = m.hexdigest()
    return encodeStr

# print(md5("123456"))