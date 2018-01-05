import re

# 预编译正则表达式
re_complie_00 = re.compile(r'^(\d{3})-(\d{3,8})$')
index_00 = re_complie_00.match("010-12345").groups()
print(index_00)

# 1-
regular_00 = r"[0-9]+abc"
test_00 = "123Abc"

index_00 = re.match(regular_00,test_00,flags=re.I)
print(index_00.group())