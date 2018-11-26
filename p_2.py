from functools import lru_cache


@lru_cache(maxsize=64)
def fib(n):
    if n <= 2:
        return n
    return fib(n - 1) + fib(n - 2)


def run():
    r = list(filter(lambda n: n % 2 == 0 and n < 4_000_000, map(fib, range(1, 100))))
    print(sum(r))


if __name__ == '__main__':
    run()
