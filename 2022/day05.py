import sys
sys.path.append('..')

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def part1():
    stacksCopy = [[x for x in stack] for stack in stacks]

    for instruction in instructions:
        count = int(instruction.split(' ')[1])
        indexFrom = int(instruction.split(' ')[3]) - 1
        indexTo = int(instruction.split(' ')[5]) - 1

        for _ in range(count):
            stacksCopy[indexTo].append(stacksCopy[indexFrom].pop())
    
    print(f'solution to part 1: {"".join(map(lambda stack: stack[-1], stacksCopy))}')


def part2():
    stacksCopy = [[x for x in stack] for stack in stacks]

    for instruction in instructions:
        count = int(instruction.split(' ')[1])
        indexFrom = int(instruction.split(' ')[3]) - 1
        indexTo = int(instruction.split(' ')[5]) - 1

        stacksCopy[indexTo].extend(stacksCopy[indexFrom][-count:])
        stacksCopy[indexFrom] = stacksCopy[indexFrom][:-count]

    print(f'solution to part 2: {"".join(map(lambda stack: stack[-1], stacksCopy))}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    blank_line_index = dataStr.index('')
    stacks_count = 1 + dataStr[blank_line_index - 2].count(' ')
    
    stacks = [[] for _ in range(stacks_count)]
    
    for level in range(blank_line_index - 2, -1, -1):
        for s in range(stacks_count):
            value = dataStr[level][4 * s + 1]
            if value != ' ':
                stacks[s].append(value)

    instructions = dataStr[blank_line_index + 1:]

    part1()

    part2()
