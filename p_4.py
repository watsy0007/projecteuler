def is_palindromic(x, y):
    v = str(x * y)
    return v == v[::-1]


def gen_palindromic(max_value):
    for x in range(max_value, 1, -1):
        for y in range(max_value, x, -1):
            if is_palindromic(x, y):
                yield x * y, x, y


def run():
    print(max(list(map(lambda x: x[0], gen_palindromic(999)))))


def test():
    assert is_palindromic(91, 99)
    assert 9009 == max(list(map(lambda x: x[0], gen_palindromic(99))))


if __name__ == '__main__':
    run()
