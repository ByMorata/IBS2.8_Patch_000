import os
import io
import shutil

path_00 = r'D:\0_Install\OneDrive\00_日常处理\2016年06月01日 大学毕业设计文档及其源码\毕业论文及毕业设计制作规范（金山学院）'
flag_00 = 0
dict_00 = {}

def get_dir(path, flag_00=0):
    string_00 = [str for str in os.listdir(path) if not os.path.isdir(os.path.join(path, str))]

    for value in string_00:
        dict_00["_" + str(flag_00) +
                "_" + value] = value

    string_01 = [str for str in os.listdir(path) if os.path.isdir(os.path.join(path, str))]

    for value in string_01:
        get_dir(os.path.join(path, value), flag_00 + 1)

    with open(r".\1000_files.txt", "w", encoding="UTF-8", errors="ignore") as file_00:
        for value in dict_00:
            file_00.write(value+"\r")

get_dir(path_00)
