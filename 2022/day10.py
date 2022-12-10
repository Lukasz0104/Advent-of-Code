import sys
sys.path.append('..')

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def part1():
    ticks = [20 + 40 * i for i in range(6)]
    result = 0
    x = 1
    tick = 1

    for line in dataStr:
        tick += 1
        if line != 'noop':
            if tick in ticks:
                result += tick * x    

            tick += 1
            x += int(line.split(' ')[1])
        
        if tick in ticks:
            result += tick * x

    print(f'solution to part 1: {result}')


def part2():
    pos = 0
    sprite_pos = 1
    row = ''

    print('solution to part 2:')
    for line in dataStr:
        pos += 1
        if pos in range(sprite_pos, sprite_pos + 3):
            row += '#'
        else:
            row += ' '

        if len(row) == 40:
            print(row)
            row = ''
            pos = 0

        if line != 'noop':
            pos += 1

            if pos in range(sprite_pos, sprite_pos + 3):
                row += '#'
            else:
                row += ' '

            sprite_pos += int(line.split(' ')[1])

        if len(row) == 40:
            print(row)
            row = ''
            pos = 0


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    part1()

    part2()
