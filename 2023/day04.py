import sys
sys.path.append("..")
from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def part1():
    result = 0
    for line in dataStr:
        common_count = count_matches(line)
        if common_count > 0:
            result += 2 ** (common_count - 1)

    print(f"solution to part 1: {result}")


def count_matches(line: str) -> int:
    numbers = line.split(": ")[1]
    winning_part, my_part = numbers.split(" | ")

    winning_nums = set(filter(lambda x: x, winning_part.split(" ")))
    my_nums = set(filter(lambda x: x, my_part.split(" ")))
    return len(my_nums.intersection(winning_nums))


def part2():
    copy_counts = {(i + 1): 1 for i in range(len(dataStr))}
    for key in copy_counts.keys():
        count = count_matches(dataStr[key - 1])
        for _ in range(copy_counts[key]):
            for i in range(count):
                copy_counts[key + i + 1] += 1

    print(f"solution to part 2: {sum(copy_counts.values())}")


if __name__ == "__main__":
    dataStr = readData(DAY, YEAR)

    part1()

    part2()
