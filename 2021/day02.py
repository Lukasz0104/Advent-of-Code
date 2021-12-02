from readData import readData
DAY = __file__[-5:-3]


def part1():
    position = depth = 0
    for d in data:
        command, x = d
        if command == 'forward':
            position += x
        elif command == 'down':
            depth += x
        elif command == 'up':
            depth -= x

    print(position * depth)


def part2():
    position = depth = aim = 0
    for d in data:
        command, x = d
        if command == 'down':
            aim += x
        elif command == 'up':
            aim -= x
        elif command == 'forward':
            position += x
            depth += aim * x

    print(position * depth)


if __name__ == '__main__':
    data = [(lambda x: (lambda a, b: tuple([a, int(b)]))(*x.split(' ')))(x)
            for x in readData(DAY)]

    part1()

    part2()
