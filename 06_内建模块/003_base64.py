import base64

value_00 = base64.b64encode(b"Hello World")
print(value_00)

value_01 = base64.b64decode(b'SGVsbG8gV29ybGQ=')
print(value_01)

value_02 = base64.b64encode("测试在Python下使用.".encode("UTF-8"))
print(value_02)

value_03 = base64.b64decode(value_02).decode("UTF-8")
print(value_03)

value_04 = "测试字符串".encode("UTF-8")
print(value_04)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)
