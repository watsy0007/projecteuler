# from math import pow


def run():
    r = pow(2, 1_000)
    print(sum(map(int, str(r))))


if __name__ == '__main__':
    run()

# python p_16.py  0.01s user 0.01s system 68% cpu 0.036 total
