import sys
from copy import deepcopy
from typing import List, Tuple

sys.path.append('..')

from AoCUtils import readData

DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


class Monkey:
    def __init__(self, 
                 starting_items: List[int], 
                 op: Tuple[str, str], 
                 testValue: int, 
                 target1: int, 
                 target2: int):
        self.items: List[int] = starting_items
        self.operationParams: Tuple[str, str] = op
        self.testValue = testValue
        self.targetPositive = target1
        self.targetNegative = target2
        self.inspectedItems = 0

    def operation(self, x: int) -> int:
        if self.operationParams[0] == '+':
            return x + int(self.operationParams[1])
        elif self.operationParams[0] == '*':
            if self.operationParams[1] == 'old':
                return x * x
            else:
                return x * int(self.operationParams[1])

    def inspect(self, divide = True) -> Tuple[int, int]:
        self.inspectedItems += 1
        item = self.operation(self.items.pop(0))

        if divide:
            item //= 3
        else:
            item %= LCM

        if self.test(item):
            return item, self.targetPositive
        else:
            return item, self.targetNegative

    def test(self, x: int) -> bool:
        return x % self.testValue == 0
    
    def __repr__(self) -> str:
        return f'Monkey(items={self.items}, targetPositive={self.targetPositive}, targetNegative={self.targetNegative})'


def part1():
    for _ in range(20):
        for monkey in monkeys1:
            while monkey.items:
                item, target = monkey.inspect()
                monkeys1[target].items.append(item)

    top2 = sorted(map(lambda m : m.inspectedItems, monkeys1))[-2:]
    res = top2[0] * top2[1]
    print(f'solution to part 1: {res}')


def part2():
    for _ in range(10000):
        for monkey in monkeys2:
            while len(monkey.items) > 0:
                item, target = monkey.inspect(False)
                monkeys2[target].items.append(item)


    top2 = sorted(map(lambda m : m.inspectedItems, monkeys2), reverse=True)
    res = top2[0] * top2[1]
    print(f'solution to part 2: {res}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    monkeys1: List[Monkey] = []
    monkeys2: List[Monkey] = []

    LCM = 1

    i = 0
    while i < len(dataStr):
        line = dataStr[i]
        if line.startswith('Monkey'):
            items = [int(item) for item in dataStr[i + 1].lstrip().replace('Starting items: ', '').split(', ')]

            operationParams = dataStr[i + 2].lstrip().split(' ')[-2:]

            testValue = int(dataStr[i + 3].lstrip().lstrip().split(' ')[-1])
            LCM *= testValue

            targetPositive = int(dataStr[i + 4].lstrip().split(' ')[-1])
            targetNegative = int(dataStr[i + 5].lstrip().split(' ')[-1])

            monkeys1.append(Monkey(items, operationParams, testValue, targetPositive, targetNegative))
            monkeys2.append(Monkey(deepcopy(items), operationParams, testValue, targetPositive, targetNegative))
            i += 5
        i += 1

    part1()

    part2()
