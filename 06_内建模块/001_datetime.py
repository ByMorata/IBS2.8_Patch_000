# 导入datetime标准库下datetime的类
from datetime import datetime  # 时间类
from datetime import timedelta  # 导入时间计算

# 获取当前的日期时间
flag_00 = datetime.now()
print(flag_00)

# 获取特定的日期时间
flag_01 = datetime(2015, 12, 12, 12, 32, 11)
print(flag_01)

# 正常的时间转换为timestamp时间(秒表)
flag_02 = flag_01.timestamp()
print(int(flag_02))

# timestamp时间(秒表)转换为正常得时间
flag_03 = datetime.fromtimestamp(flag_02 + 3)
print(flag_03)

# 转换为UTC标准时间
flag_04 = datetime.utcfromtimestamp(flag_02 + 3)
print(flag_04)

# str转换为datetime
flag_05 = datetime.strptime("2015-12-31 12:21:31", "%Y-%m-%d %H:%M:%S")
print(flag_05)
# 时间格式参考Python文档
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

# datetime转换为str
flag_06 = flag_05.strftime("%a, %b %d %H:%M")
print(flag_06)

# datetime加减
# 加法
flag_07 = datetime(year=9999, month=12, day=1)
flag_08 = flag_07 + timedelta(hours=10, days=12, minutes=12, weeks=1)
print(flag_08)
# 减法
flag_09 = flag_07 - timedelta(hours=1)
print(flag_09)
