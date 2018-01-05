import hashlib

md5_00 = hashlib.md5()
md5_00.update("Hello World!!!!".encode("UTF-8"))
print(md5_00.hexdigest())


md5_01 = hashlib.md5()
md5_01.update("Hello ".encode("UTF-8"))
md5_01.update("World!!!!".encode("UTF-8"))
print(md5_01.hexdigest())


sha1_00 = hashlib.sha1()
sha1_00.update("Hello World!!!!".encode("UTF-8"))
print(sha1_00.hexdigest())

sha1_00 = hashlib.sha1()
sha1_00.update("Hello ".encode("UTF-8"))
sha1_00.update("World!!!!".encode("UTF-8"))
print(sha1_00.hexdigest())


