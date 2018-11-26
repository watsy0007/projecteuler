def run():
    largest = 2
    number = 2
    for i in range(2, 1_000_000):
        chain_length = 1
        sequence = i
        while sequence != 1:
            if sequence % 2 == 0:
                sequence = sequence // 2
            else:
                sequence = 3 * sequence + 1
            chain_length += 1
        if chain_length > largest:
            largest = chain_length
            number = i
    print(largest, number)


if __name__ == '__main__':
    run()


# python p_14.py  19.41s user 0.04s system 99% cpu 19.502 total
