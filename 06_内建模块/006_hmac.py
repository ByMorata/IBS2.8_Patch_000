import hmac, struct


key_00 = b"secret"

string_00 = struct.pack(b">s", b"Hello World!")
print(type(string_00))

hex_00 = hmac.new(key_00, string_00, digestmod="MD5")
print(hex_00.hexdigest())
