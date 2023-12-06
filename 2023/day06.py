import sys
sys.path.append('..')
import math

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def part1():
    result = 1
    for (t, d) in zip(times, distances):
        x1, x2 = solve_quadratic(-1, int(t), -int(d))
        result *= math.floor(x2) - math.floor(x1)

    print(f'solution to part 1: {result}')


def part2():
    time = int(''.join(times))
    distance = int(''.join(distances))

    x1, x2 = solve_quadratic(-1, time, -distance)

    if (x1 > x2):
        x1, x2 = x2, x1

    result = math.floor(x2) - math.floor(x1)

    print(f'solution to part 2: {result}')


def solve_quadratic(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0: return []

    delta_root = math.sqrt(delta)

    r1 = (-b - delta_root) / (2 * a)
    r2 = (-b + delta_root) / (2 * a)

    return [r1, r2]


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    times = dataStr[0].split()[1:]
    distances = dataStr[1].split()[1:]

    part1()

    part2()
