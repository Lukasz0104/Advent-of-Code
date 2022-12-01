import sys
sys.path.append('..')

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]

def part1():
    res = max(map(sum, data))
    print(f'solution to part 1: {res}')

def part2():
    res = sum(sorted(map(sum, data))[-3:])
    print(f'solution to part 2: {res}')

if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    data = []
    currentList = []

    for s in dataStr:
        if s == '':
            data.append(currentList)
            currentList = []
        else:
            currentList.append(int(s))
    data.append(currentList)
    
    part1()

    part2()
