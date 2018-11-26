from utils import is_prime


def run():
    print(sum(filter(is_prime, range(2, 2_000_000))))


if __name__ == '__main__':
    run()

# python p_10.py  7.15s user 0.02s system 99% cpu 7.196 total
