import sys
from typing import List, Literal, Tuple
sys.path.append('..')

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]

Tile = Literal['.'] | Literal['#'] | Literal['o']
Cave = List[List[Tile]]

def nextPosition(x: int, y: int, cv: Cave) -> Tuple[int, int] | None:
    if x < minX or x > maxX:
        return None

    while cv[y + 1][x - minX] == '.':
        y += 1
        if y + 1 > maxY:
            return None

    if x - minX - 1 < 0:
        return None
    elif cv[y + 1][x - minX - 1] == '.':
        return nextPosition(x - 1, y + 1, cv)
    
    if x - minX + 1 >= maxX:
        return None
    elif cv[y + 1][x - minX + 1] == '.':
        return nextPosition(x + 1, y + 1, cv)

    return (x, y)


def nextPositionWithFloor(x: int, y: int) -> Tuple[int, int]:
    global minX, maxX
    if y + 1 == maxY:
        return (x, y)

    while cave[y + 1][x - minX] == '.':
        y += 1

    if cave[y + 1][x - minX - 1] == '.':
        return nextPositionWithFloor(x - 1, y + 1)
    
    if cave[y + 1][x - minX + 1] == '.':
        return nextPositionWithFloor(x + 1, y + 1)

    return (x, y)


def part1():
    caveCopy: Cave = [[x for x in row] for row in cave]
    count = 0
    while (pos := nextPosition(500, 0, caveCopy)) != None:
        x, y = pos
        caveCopy[y][x - minX] = 'o'
        count += 1

    print(f'solution to part 1: {count}')


def part2():
    global minX, maxX, maxY
    count = 0

    minX -= 2
    maxX += 2
    maxY += 2

    for i in range(len(cave)):
        cave[i].insert(0, '.')
        cave[i].insert(0, '.')
        cave[i].append('.')
        cave[i].append('.')
    
    cave.append(['.' for _ in range(len(cave[0]))])
    cave.append(['#' for _ in range(len(cave[0]))])

    while (pos := nextPositionWithFloor(500, 0)) != (500, 0):
        x, y = pos
        count += 1
        cave[y][x - minX] = 'o'
        if x == minX or x == maxX:
            for i in range(len(cave)):
                cave[i].insert(0, '.')
                cave[i].append('.')
            cave[-1][0] = '#'
            cave[-1][-1] = '#'
            minX -= 1
            maxX += 1

    print(f'solution to part 2: {count + 1}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    minX = -1
    maxX = -1

    minY = -1
    maxY = -1

    for line in dataStr:
        values = line.split(' -> ')
        for value in values:
            x,y = [int(v) for v in value.split(',')]
            if minX == -1 or x < minX:
                minX = x
            if maxX == -1 or x > maxX:
                maxX = x
            if minY == -1 or y < minY:
                minY = y
            if maxY == -1 or y > maxY:
                maxY = y

    cave: Cave = [['.' for _ in range(minX, maxX + 1)] for _ in range(maxY + 1)]

    for line in dataStr:
        values = line.split(' -> ')
        
        for i in range(1, len(values)):
            x1, y1 = [int(v) for v in values[i - 1].split(',')]
            x2, y2 = [int(v) for v in values[i].split(',')]

            if x1 > x2:
                x1, x2 = x2, x1
            
            if y1 > y2:
                y1, y2 = y2, y1
            
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    cave[y][x - minX] = '#'

    part1()

    part2()
