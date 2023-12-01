#!/usr/bin/env python3
import sys
import re
sys.path.append('..')

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def part1():
    result = 0
    regex = r"\D"
    for line in dataStr:
        digits_only = re.sub(regex, '', line)
        if digits_only:
            result += int(digits_only[0] + digits_only[-1])
    print(f'solution to part 1: {result}')


def part2():
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    patterns = list(digits.keys()) + [f"{i}" for i in range(1, 10)]
    result = 0
    for line in dataStr:
        # For each pattern return index of first occurence and filter out negative indices
        indexes = list(
            filter(
                lambda x: x[1] >= 0,
                map(
                    lambda pattern: (
                        pattern,
                        line.find(pattern),
                    ),  # return pair: (pattern, index)
                    patterns
                ),
            )
        )
        # Similarly, find index of last occurence
        last_indexes = list(
            map(lambda pattern: (pattern, line.rfind(pattern)), patterns)
        )

        # Find min and max by pattern
        firstIndex = min(indexes, key=lambda x: x[1])
        lastIndex = max(last_indexes, key=lambda x: x[1])

        # Retrieve value for pattern, or if pattern is already a digit return it
        firstDigit = int(digits.get(firstIndex[0], firstIndex[0]))
        lastDigit = int(digits.get(lastIndex[0], lastIndex[0]))

        result += int(10 * firstDigit + lastDigit)
    print(f"solution to part 2: {result}")



if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    part1()

    part2()
