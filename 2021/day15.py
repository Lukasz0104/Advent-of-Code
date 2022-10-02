from copy import deepcopy
from typing import Dict, Iterable, Tuple
from AoCUtils import GREEN, RED, RESET, readData

DAY = __file__[-5:-3]


def part1():
    distance = findPathWithMinRisk(data)
    print(f'solution to part 1: {distance}')


def calculatePathDistance(x: int, y: int, previousPoints: Dict[Tuple[int, int], Tuple[int, int]], riskLevelMap: Iterable[Iterable[int]]) -> int:
    """Traverse map to point (0, 0) and calculate total risk.

    Args:
        x (int): starting x position
        y (int): starting y position
        previousPoints (Dict[Tuple[int, int], Tuple[int, int]]): Dictionary mapping each point to previous point (with shortest path)
        riskLevelMap (Iterable[Iterable[int]]): 2 dimensional iterable of risk levels

    Returns:
        int: Total risk of the path.
    """
    distance = 0

    while (x, y) != (0, 0):
        distance += riskLevelMap[y][x]
        x, y = previousPoints[(x, y)]

    return distance


def printPath(startX, startY, previousPoints, riskMap):
    path = [(0, 0)]
    while (startX, startY) != (0, 0):
        path.append((startX, startY))
        startX, startY = previousPoints[(startX, startY)]

    for y in range(len(riskMap)):
        for x in range(len(riskMap[0])):
            print(f'{GREEN if (x,y) in path else RED}{riskMap[y][x]}', end='')
        print(RESET)


def findPathWithMinRisk(riskMap: Iterable[Iterable[int]]) -> int:
    SizeX = len(riskMap[0])
    SizeY = len(riskMap)

    previous_points = {(x, y): (-1, -1) for x in range(SizeX) for y in range(SizeY)}
    previous_points[(0, 0)] = (0, 0)

    queue = [(0, 0)]

    while len(queue) > 0:
        x, y = queue.pop(0)
        currentDistance = calculatePathDistance(x, y, previous_points, riskMap)

        for dx in (-1, 1):
            if x + dx in (-1, SizeX):
                continue

            if previous_points[(x + dx, y)] == (-1, -1):
                previous_points[(x + dx, y)] = (x, y)
            else:
                d = calculatePathDistance(x + dx, y, previous_points, riskMap)

                if currentDistance + riskMap[y][x + dx] <= d:
                    previous_points[(x + dx, y)] = (x, y)

        for dy in (-1, 1):
            if y + dy in (-1, SizeY):
                continue

            if previous_points[(x, y + dy)] == (-1, -1):
                previous_points[(x, y + dy)] = (x, y)
            else:
                d = calculatePathDistance(x, y + dy, previous_points, riskMap)

                if currentDistance + riskMap[y + dy][x] <= d:
                    previous_points[(x, y + dy)] = (x, y)

        for dx in (0, 1):
            if x + dx == SizeX:
                continue
            for dy in (0, 1):
                if dx == dy:
                    continue
                if y + dy == SizeY:
                    continue
                if (x + dx, y + dy) in queue:
                    continue
                queue.append((x + dx, y + dy))

    if printPathFlag:
        printPath(SizeX - 1, SizeY - 1, previous_points, riskMap)

    return calculatePathDistance(SizeX - 1, SizeY - 1, previous_points, riskMap)


def part2(printExpandedMap=False):
    data2 = deepcopy(data)

    # expand horizontally
    for k in range(4):
        for i in range(SIZE_Y):
            for j in range(SIZE_X):
                data2[j].append(data2[j][k * SIZE_X + i] % 9 + 1)

    # expand map vertically
    for k in range(4):
        for i in range(SIZE_Y):
            data2.append(list(map(lambda x: x % 9 + 1, data2[SIZE_Y * k + i])))

    if printExpandedMap:
        for j, row in enumerate(data2):
            for i, x in enumerate(row):
                print(f'{GREEN if (i // 10) % 2 == 1 else RED}{x}', end='')
            if j % 10 == 9:
                print('\n')
            print(RESET)

    distance = findPathWithMinRisk(data2)

    print(f'solution to part 2: {distance}')


if __name__ == '__main__':
    data = [[int(x) for x in line] for line in readData(DAY)]

    SIZE_Y = len(data)
    SIZE_X = len(data[0])

    # Change this to True to see the path
    printPathFlag = False

    part1()

    # part2 takes about 2 minutes on my machine to complete, so be patient when running for full input
    part2()
