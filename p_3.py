from math import sqrt


def is_prime(n):
    return not [i for i in range(2, int(sqrt(n)) + 1) if n % i == 0]


def prime_factors(n):
    f = 2
    large = int(sqrt(n) + 1)
    while f < large:
        if n % f == 0 and is_prime(f):
            yield f
        f += 1


def run():
    print(max(prime_factors(600_851_475_143)))


def test():
    assert 29 == max(prime_factors(13195))


if __name__ == '__main__':
    run()
