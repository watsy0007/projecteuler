# problem url https://projecteuler.net/problem=9
from math import pow


def run():
    # a < b < c and a + b + c = 1000
    # min(c) = 1000 / 3
    v = [a * b * c
         for c in range(int(1000 / 3), 1000)
         for b in range(1, c)
         for a in range(1, b)
         if a * a + b * b == c * c and a + b + c == 1000]
    print(v[0])


if __name__ == '__main__':
    run()

# python p_9.py  25.67s user 0.07s system 99% cpu 25.822 total
