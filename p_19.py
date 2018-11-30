# https://projecteuler.net/problem=19


def run():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    count = 0
    for year in range(1901, 2000):
        for idx, day_number in enumerate(days_in_month):
            number = day_number
            if idx == 1:
                if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
                    pass
                else:
                    number += 1
            days += number
            if days % 7 == 6:
                # print(year, idx + 1, number, days)
                count += 1
    print(count)


if __name__ == '__main__':
    run()


# python p_19.py  0.02s user 0.01s system 86% cpu 0.036 total
