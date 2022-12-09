import sys
from typing import Set, Tuple
sys.path.append('..')
from math import copysign

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def moveHead(direction: str, x: int, y: int) -> Tuple[int, int]:
    match direction:
        case 'R':
            x += 1
        case 'L':
            x -= 1
        case 'U':
            y += 1
        case 'D':
            y -= 1
    return (x,y)


def moveTail(x_h: int, y_h: int, x_t: int, y_t: int) -> Tuple[int, int]:
    dx = x_h - x_t
    dy = y_h - y_t

    if dx * dx + dy * dy <= 2:
        return (x_t, y_t)
    
    if dy == 0:
        x_t += copysign(1, dx)
    elif dx == 0:
        y_t += copysign(1, dy)
    else:
        x_t += copysign(1, dx)
        y_t += copysign(1, dy)

    return (x_t, y_t)


def part1():
    x_h, y_h = 0, 0
    x_t, y_t = 0, 0
    visited: Set[Tuple[int, int]] = set()
    visited.add((x_t,y_t))

    for line in dataStr:
        direction = line.split(' ')[0]
        moves = int(line.split(' ')[1])

        for _ in range(moves):
            x_h, y_h = moveHead(direction, x_h, y_h)
            x_t, y_t = moveTail(x_h, y_h, x_t, y_t)
            visited.add((x_t,y_t))

    print(f'solution to part 1: {len(visited)}')


def part2():
    rope = [(0,0)] * 9
    x_t, y_t = 0, 0
    visited: Set[Tuple[int, int]] = set()
    visited.add((x_t,y_t))

    for line in dataStr:
        direction = line.split(' ')[0]
        moves = int(line.split(' ')[1])

        for _ in range(moves):
            x_h, y_h = moveHead(direction, *rope[0])
            rope[0] = (x_h, y_h)
            for i in range(1, len(rope)):
                rope[i] = moveTail(*rope[i - 1], *rope[i])
            x_t, y_t = moveTail(*rope[-1], x_t, y_t)
            visited.add((x_t,y_t))

    print(f'solution to part 2: {len(visited)}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    part1()

    part2()
