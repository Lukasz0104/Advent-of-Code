import sys
sys.path.append('..')

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def part1():
    count = 0

    for line in dataStr:
        s1, s2 = line.split(',')

        b1, e1 = tuple(map(lambda s: int(s), s1.split('-')))
        b2, e2 = tuple(map(lambda s: int(s), s2.split('-')))

        if b1 <= b2 and e1 >= e2:
            count += 1
        elif b2 <= b1 and e2 >= e1:
            count += 1

    print(f'solution to part 1: {count}')


def part2():
    count = 0

    for line in dataStr:
        s1, s2 = line.split(',')

        b1, e1 = tuple(map(lambda s: int(s), s1.split('-')))
        b2, e2 = tuple(map(lambda s: int(s), s2.split('-')))

        if (b1 >= b2 and b1 <= e2) or (b2 >= b1 and b2 <= e1) or (e1 >= b2 and e1 <= e2) or (e2 >= b1 and e2 <= e1):
            count += 1

    print(f'solution to part 2: {count}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    part1()

    part2()
