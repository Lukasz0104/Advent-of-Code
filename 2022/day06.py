import sys
sys.path.append('..')

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def findPosition(sequenceLength: int) -> int:
    for pos in range(sequenceLength, len(data)):
        if len(set(data[pos - sequenceLength: pos])) == sequenceLength:
            return pos
    return -1


def part1():
    pos = findPosition(4)
    print(f'solution to part 1: {pos}')


def part2():
    pos = findPosition(14)
    print(f'solution to part 2: {pos}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)
    data = dataStr[0]

    part1()

    part2()
