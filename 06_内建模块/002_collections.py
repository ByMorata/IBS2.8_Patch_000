from collections import namedtuple
from collections import defaultdict
from collections import OrderedDict

option_00 = namedtuple("option", ['x', 'y'])

value_00 = option_00(x=10, y=12)
print(value_00.x)

value_01 = defaultdict(lambda: "N/A")
value_01["key_1"] = "value_1"
print(value_01[r"key_1"])
print(value_01["key_2"])

list_00 = ["value_00", "value_01"]
key = "value_03"
containsKey = 1 if key in list_00 else 0
print(containsKey)


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            print(len(self))
            last = self.popitem(last=False)
            print('remove:', last)
            OrderedDict.__setitem__(self, key, value)
        if containsKey:
            pass
        #     del self[key]
        #     print('set:', (key, value))
        else:
            print('add:', (key, value))
            OrderedDict.__setitem__(self, key, value)


value_02 = LastUpdatedOrderedDict(2)
value_02["key_00"] = "value_00"
value_02["key_01"] = "value_01"
value_02["key_01"] = "value_02"
print(value_02.get("key_00"))
print(value_02.get("key_01"))
