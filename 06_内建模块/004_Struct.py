import struct



value_00 = struct.pack(r">I",123231)
print(value_00)

value_01 = struct.unpack(r">IH",b'\xf0\xf0\xf0\xf0\x80\x80')
print(value_01)