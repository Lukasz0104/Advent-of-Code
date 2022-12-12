import sys
from typing import Dict, List, Tuple

sys.path.append('..')
from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def countSteps(x: int, y: int, previousPoints: Dict[Tuple[int, int], Tuple[int, int]], goal: Tuple[int, int] = None) -> int:
    """Counts number of steps between two points.

    Args:
        x (int): x position
        y (int): y position
        previousPoints (Dict[Tuple[int, int], Tuple[int, int]]): Dictionary mapping each point to previous point (with shortest path)
        goal (Tuple[int, int], optional): Goal position. Defaults to None.

    Returns:
        int: Number of steps in shortest path. If goal is not accessible, returns None.
    """
    if goal is None:
        goal = startPos
    d = 0
    while (x, y) != goal:
        d += 1
        if (x, y) == (-1, -1):
            return None
        x, y = previousPoints[(x, y)]
    return d


def findShortestPath(start: Tuple[int, int]):
    NOT_VISITED = (-1, -1)
    sizeX = len(heights[0])
    sizeY = len(heights)

    previousPoints = {(x, y): NOT_VISITED for x in range(len(heights[0])) for y in range(len(heights))}
    previousPoints[start] = start

    queue = [start]

    while len(queue) > 0:
        x, y = queue.pop(0)
        h = heights[y][x]
        distance = countSteps(x, y, previousPoints, start)

        for dx in (-1, 1):
            if x + dx in (-1, sizeX):
                continue
            key = (x + dx, y)
            if heights[y][x + dx] - h <= 1:
                if previousPoints[key] == NOT_VISITED:
                    previousPoints[key] = (x, y)
                    queue.append(key)
                else:
                    d = countSteps(*key, previousPoints, start)

                    if d is None: 
                        return None

                    if distance + 1 < d:
                        previousPoints[key] = (x, y)
        
        for dy in (-1, 1):
            if y + dy in (-1, sizeY):
                continue
            key = (x, y + dy)
            if heights[y + dy][x] - h <= 1:
                if previousPoints[key] == NOT_VISITED:
                    previousPoints[key] = (x, y)
                    queue.append(key)
                else:
                    d = countSteps(*key, previousPoints, start)

                    if d is None: 
                        return None

                    if distance + 1 < d:
                        previousPoints[key] = (x, y)

    return countSteps(*goalPos, previousPoints, start)


def part1():
    res = findShortestPath(startPos)
    print(f'solution to part 1: {res}')


def part2():
    minSteps = None
    for j, row in enumerate(heights):
        for i, h in enumerate(row):
            if h == 0:
                d = findShortestPath((i, j))
                if d is None: 
                    continue
                if minSteps is None or d < minSteps:
                    minSteps = d
    print(f'solution to part 2: {minSteps}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    heights: List[List[int]] = []

    startPos = None
    goalPos = None

    for j, row in enumerate(dataStr):
        current = []
        for i, h in enumerate(row):
            if h == 'S':
                current.append(0)
                startPos = (i, j)
            elif h == 'E':
                current.append(ord('z') - ord('a'))
                goalPos = (i, j)
            else:
                current.append(ord(h) - ord('a'))
        heights.append(current)

    part1()

    # part2 may take up to 40 seconds
    part2()
