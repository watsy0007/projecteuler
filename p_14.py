def run():
    largest = 2
    for i in range(2, 1_000_000):
        chain_length = 1  # 1 and self
        sequence = i
        while sequence != 1:
            if sequence % 2 == 0:
                sequence = sequence // 2
            else:
                sequence = 3 * sequence + 1
            chain_length += 1
        if chain_length > largest:
            largest = chain_length
    print(largest)


if __name__ == '__main__':
    run()


# python p_14.py  20.01s user 0.07s system 99% cpu 20.203 total
