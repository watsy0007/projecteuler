from math import sqrt
from functools import reduce
from operator import mul


# https://zh.wikipedia.org/wiki/埃拉托斯特尼筛法
def is_prime(n: int) -> bool:
    # not even
    if n % 2 == 0:
        if n != 2:
            return False
        return True
    # 3, 5, 7, 9 ...
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True


def reduce_mul(value):
    return reduce(mul, map(int, value))
