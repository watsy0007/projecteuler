# https://projecteuler.net/problem=15

from utils import factorial


# method 1
# from itertools import permutations
# def count_lattice_path(n):
#     # 0 right / 1 down
#     numbers = list(map(lambda x: 0 if x % 2 == 0 else 1, range(0, n)))
#     paths = set()
#     for route in permutations(numbers, n):
#         v = route[0] * 1000 + route[1] * 100 + route[2] * 10 + route[3]
#         if v in paths:
#             continue
#         paths.add(v)
#     return len(paths)

# method 2
def count_lattice_path(n, m):
    return factorial(n + m) // (factorial(n) * factorial(m))


def run():
    print(count_lattice_path(20, 20))


if __name__ == '__main__':
    run()


# python p_15.py  0.02s user 0.01s system 90% cpu 0.028 total