import sys
sys.path.append("..")
import re
import typing
import functools

from AoCUtils import readData

DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]

Position = typing.Tuple[int, int]

directions = [
    (x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == 0 and y == 0)
]

def part1():
    symbol_positions: typing.Set[Position] = set()
    symbol_regex = re.compile("[^\d.]")
    for row, line in enumerate(dataStr):
        matches = list(symbol_regex.finditer(line))
        for m in matches:
            symbol_positions.add((row, m.start()))

    digit_positions: typing.Set[Position] = set()

    for row, col in symbol_positions:
        for x, y in directions:
            if dataStr[row + x][col + y].isdigit():
                pos = getPositionOfFirstDigit(row + x, col + y)
                digit_positions.add(pos)

    result = 0
    for pos in digit_positions:
        result += getNumberAtPos(*pos)

    print(f"solution to part 1: {result}")


def getPositionOfFirstDigit(row: int, col: int) -> Position:
    while col - 1 >= 0 and dataStr[row][col - 1].isdigit():
        col -= 1
    return (row, col)


def getNumberAtPos(row: int, col: int) -> int:
    max_column = len(dataStr[0])
    num = int(dataStr[row][col])
    while col + 1 < max_column and dataStr[row][col + 1].isdigit():
        col += 1
        num = 10 * num + int(dataStr[row][col])
    return num


def part2():
    gear_positions: typing.Set[Position] = set()
    gear_regex = re.compile("[*]")
    for row, line in enumerate(dataStr):
        matches = list(gear_regex.finditer(line))
        for m in matches:
            gear_positions.add((row, m.start()))

    result = 0
    for row, col in gear_positions:
        positions = set()
        for x, y in directions:
            if dataStr[row + x][col + y].isdigit():
                pos = getPositionOfFirstDigit(row + x, col + y)
                positions.add(pos)

        if len(positions) == 2:
            first_digit_positions = map(
                lambda p: getPositionOfFirstDigit(*p), positions
            )
            numbers = map(lambda x: getNumberAtPos(*x), first_digit_positions)

            result += functools.reduce(lambda a, b: a * b, numbers, 1)

    print(f"solution to part 2: {result}")


if __name__ == "__main__":
    dataStr = readData(DAY, YEAR)

    part1()

    part2()
