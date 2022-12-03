import sys
sys.path.append('..')

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def getPriority(letter: str):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

def part1():
    prioritySum = 0
    for line in data:
        l = len(line)
        for letter in (set(line[:l // 2]) & set(line[l // 2 :])):
            prioritySum += getPriority(letter)

    print(f'solution to part 1: {prioritySum}')

def part2():
    prioritySum = 0
    for groupNo in range(0, len(data), 3):
        badge = (set(data[groupNo]) & set(data[groupNo + 1]) & set(data[groupNo + 2])).pop()
        prioritySum += getPriority(badge)

    print(f'solution to part 2: {prioritySum}')

if __name__ == '__main__':
    data = readData(DAY, YEAR)

    part1()

    part2()
