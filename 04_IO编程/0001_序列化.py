import os
import io
import pickle


dict_00 = dict(name="Jason Morata", age=18, sex="female")
string_00 = pickle.dumps(dict_00)
with open(r".\1001_files.dat", "wb") as file_00:
    pickle.dump(dict_00, file_00)

dict_01 = {}
with open(r".\1001_files.dat", "rb") as file_01:
    dict_01 = pickle.load(file_01)
print(dict_01)
