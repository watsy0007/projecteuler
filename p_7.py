# https://zh.wikipedia.org/wiki/質數定理
from utils import is_prime


def prime_by_index(number, index):
    prime_index = 0
    for (idx, v) in enumerate(range(2, number)):
        if is_prime(v):
            prime_index += 1
            print(v, prime_index)
            if index == prime_index:
                return v


def run():
    print(prime_by_index(10_000_000, 10_002))  # 100 001st


if __name__ == '__main__':
    run()

# 太慢了
# python p_7.py  0.31s user 0.02s system 97% cpu 0.338 total
