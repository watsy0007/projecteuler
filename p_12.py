# https://zh.wikipedia.org/wiki/三角形數
from math import sqrt


def triangle_numbers():
    for i in range(1, 100_000_000):
        yield i * (i + 1) // 2


# method 1
# def count_divisors(number):
#     count = 0
#     if number < 2:
#         return 1
#     for i in range(2, number // 2 + 1):
#         if number % i == 0:
#             count += 1
#     return count + 2

# method 2
def count_divisors(number):
    count = 0
    if number < 2:
        return 1
    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            if number / i == i:
                count += 1
            else:
                count += 2
    return count


def run():
    for i in triangle_numbers():
        if count_divisors(i) > 500:
            print(i)
            break


if __name__ == '__main__':
    run()

# python p_12.py  4.18s user 0.02s system 99% cpu 4.241 total
