import sys
sys.path.append('..')
import re

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def part1():
    result = 0
    pattern = r'^Game (\d+): (((((\d|(1[012])) red)|((\d|(1[0123])) green)|((\d|(1[01234])) blue))(, )*)+(; )?)+$'
    regex = re.compile(pattern)
    for line in dataStr:
        if m := regex.match(line):
            result += int(m.group(1))
    print(f'solution to part 1: {result}')


def part2():
    result = 0

    pattern_red = re.compile(r'(\d+) red')
    pattern_green = re.compile(r'(\d+) green')
    pattern_blue = re.compile(r'(\d+) blue')

    for line in dataStr:
        red_matches = pattern_red.findall(line)
        max_red = max(map(int, red_matches))

        green_matches = pattern_green.findall(line)
        max_green = max(map(int, green_matches))

        blue_matches = pattern_blue.findall(line)
        max_blue = max(map(int, blue_matches))

        result += max_red * max_green * max_blue

    print(f'solution to part 2: {result}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    part1()

    part2()
