import sys
sys.path.append('..')

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def isVisible(x: int, y: int) -> bool:
    val = data[y][x]
    current_highest = 0
    
    for i in range(x):
        if data[y][i] > current_highest:
            current_highest = data[y][i]
    
    if current_highest < val: 
        return True

    current_highest = 0
    for i in range(sizeX - 1, x, -1):
        if data[y][i] > current_highest:
            current_highest = data[y][i]

    if current_highest < val: 
        return True
    
    current_highest = 0
    for i in range(y):
        if data[i][x] > current_highest:
            current_highest = data[i][x]
    if current_highest < val: 
        return True
    
    current_highest = 0
    for i in range(sizeY - 1, y, -1):
        if data[i][x] > current_highest:
            current_highest = data[i][x]

    return current_highest < val


def calculateScore(x: int, y: int) -> int:
    val = data[y][x]
    score = 1
    current_multiplier = 0

    for i in range(x - 1, -1, -1):
        current_multiplier += 1
        if data[y][i] >= val: 
            break

    score *= current_multiplier
    current_multiplier = 0

    for i in range(x + 1, sizeX):
        current_multiplier += 1
        if data[y][i] >= val: 
            break

    score *= current_multiplier
    current_multiplier = 0

    for i in range(y - 1, -1, -1):
        current_multiplier += 1
        if data[i][x] >= val:
            break
    
    score *= current_multiplier
    current_multiplier = 0

    for i in range(y + 1, sizeY):
        current_multiplier += 1
        if data[i][x] >= val:
            break
    
    score *= current_multiplier
    return score


def part1():
    count = 2 * sizeX + 2 * (sizeY - 2)

    for y in range(1, sizeY - 1):
        for x in range(1, sizeX - 1):
            if isVisible(x, y):
                count += 1

    print(f'solution to part 1: {count}')


def part2():
    highest_score = 0

    for y in range(1, sizeY - 1):
        for x in range(1, sizeX - 1):
            score = calculateScore(x, y)
            if score > highest_score:
                highest_score = score

    print(f'solution to part 2: {highest_score}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)
    data = tuple(tuple(int(x) for x in row) for row in dataStr)

    sizeX = len(data[0])
    sizeY = len(data)

    part1()

    part2()
