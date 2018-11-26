from functools import reduce
from itertools import product


# (a + b + ... + n) ^ 2 - (a ^ 2 + b ^ 2 + ... + n ^ 2)
# (a * b + a * c + ... + a * n) + ( b * a + b + c + ... + b * n) + ...
def calc(n):
    return reduce(lambda a, b: a + b[0] * b[1], filter(lambda v: v[0] != v[1], product(range(1, n), range(1, n))), 0)


def run():
    print(calc(101))


def test():
    assert 2640, calc(11)


if __name__ == '__main__':
    run()
