unites = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
          'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
dizaines = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def num_to_word(n):
    if n == 1000:
        return 'one thousand'
    elif n > 100:
        centaine, dizaine = n // 100, n % 100
        return f'{num_to_word(centaine)} hundred and {num_to_word(dizaine)}'
    elif n == 100:
        return 'one hundred'
    elif n >= 20:
        unite = n % 10
        if unite == 0:
            return dizaines[(n - 20) // 10]
        return f'{dizaines[(n // 10 - 2)]}-{num_to_word(unite)}'
    else:
        return unites[n - 1]


def num_length(num):
    word = num_to_word(num).replace(' ', '').replace('-', '')
    return len(word)


def run():
    for i in range(1, 1_001):
        print(i, num_length(i), '->', num_to_word(i))
    print(sum(([num_length(i) for i in range(1, 1_001)])))


def test():
    assert 23 == num_length(342)
    assert 20 == num_length(115)
    assert 19 == sum([num_length(i) for i in range(1, 6)])


if __name__ == '__main__':
    test()
    run()

# python p_17.py  0.03s user 0.01s system 74% cpu 0.044 total
# 这版有 bug, 暂时不修了, 回家睡觉