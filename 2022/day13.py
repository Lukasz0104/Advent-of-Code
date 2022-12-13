import copy
import sys
from typing import List, Union
from functools import cmp_to_key

sys.path.append('..')
from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


Packet = List[Union[int, 'Packet']]

def isProperOrder(p1: Packet, p2: Packet) -> bool:
    if len(p1) == 0 and len(p2) > 0:
        return True
    if len(p1) > 0 and len(p2) == 0:
        return False
    if len(p1) == 0 and len(p2) == 0:
        return True

    v1 = p1[0]
    v2 = p2[0]

    if isinstance(v1, int) and isinstance(v2, int):
        if (c := v1 - v2) != 0:
            return c < 0
        return isProperOrder(p1[1:], p2[1:])
    elif isinstance(v1, int) and isinstance(v2, list):
        p1_new = [ [v1], *p1[1:] ]
        return isProperOrder(p1_new, p2)
    elif isinstance(v1, list) and isinstance(v2, int):
        p2_new = [ [v2], *p2[1:] ]
        return isProperOrder(p1, p2_new)
    elif isinstance(v1, list) and isinstance(v2, list):
        i = 0
        while i < len(v1) and i < len(v2):
            x1 = v1[i]
            x2 = v2[i]
            i += 1
            if isinstance(x1, int) and isinstance(x2, int):
                if (c := x1 - x2) != 0:
                    return c < 0
            else: 
                return isProperOrder([x1], [x2])
        
        if len(v1) < len(v2): return True
        elif len(v1) > len(v2): return False
        
        return isProperOrder(p1[1:], p2[1:])


def part1():
    result = 0
    for index, packet in enumerate(copy.deepcopy(packets)):
        if isProperOrder(*packet):
            result += index + 1
    print(f'solution to part 1: {result}')


def part2():
    cmp = lambda p1, p2 : -1 if isProperOrder(p1, p2) else 1
    ordered = [ [[2]], [[6]] ]
    
    for p in packets:
        left, right = p
        ordered.append(left)
        ordered.append(right)

    ordered.sort(key=cmp_to_key(cmp))
    i1 = ordered.index([[2]]) + 1
    i2 = ordered.index([[6]]) + 1

    print(f'solution to part 2: {i1 * i2}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    packets = []

    for i in range(0, len(dataStr), 3):
        left = eval(dataStr[i])
        right = eval(dataStr[i + 1])

        packets.append( (left, right) )

    part1()

    part2()
