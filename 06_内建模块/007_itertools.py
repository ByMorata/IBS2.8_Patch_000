import itertools
from functools import reduce


# list_01 = itertools.takewhile(lambda x: x > 1, itertools.count(1))
#
# list_00 = itertools.count(1)
#
# for value_00 in list_01:
#     print(value_00)


def get_pi(pi_00):
    list_00 = [x for x in range(2 * pi_00) if x % 2 != 0]
    list_01 = itertools.cycle((4, -4))


    sum_00 = sum((next(list_01) / x) for x in list_00)
    print(sum_00)

if __name__ == '__main__':
    get_pi(100000)
