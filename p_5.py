# https://zh.wikipedia.org/wiki/最小公倍數
# https://zh.wikihow.com/求两个数的最小公倍数

from functools import reduce


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def run():
    print(reduce(lcm, range(1, 21)))


def test():
    assert 2520 == reduce(lcm, range(1, 11))


if __name__ == '__main__':
    run()
