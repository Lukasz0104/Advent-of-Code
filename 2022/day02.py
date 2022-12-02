import sys
sys.path.append('..')

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]

DRAW = 3
WON = 6


def getRoundResult(opponentGuess: int, myGuess: int) -> int:
    match (opponentGuess, myGuess):
        case (1, 1) | (2, 2) | (3, 3): return DRAW
        case (1, 3) | (3, 2) | (2, 1): return 0
        case (1, 2) | (2, 3) | (3, 1): return WON

def part1():
    scores = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    score = 0

    for r in data:
        opponent = scores[r[0]]
        my = scores[r[1]]

        score += my + getRoundResult(opponent, my)

    print(f'solution to part 1: {score}')

def part2():
    scores = {
        'A': 1,
        'B': 2,
        'C': 3,
    }

    score = 0

    for r in data:
        opp = scores[r[0]]
        result = r[1]
        
        if result == 'X':
            if opp == 1: score += 3
            else:
                score += opp - 1
        elif result == 'Y':
            score += opp + DRAW
        elif result == 'Z':
            if opp == 3: score += 1
            else:
                score += opp + 1
            score += WON

    print(f'solution to part 2: {score}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)
    data = list(map(lambda row: tuple(row.split(' ')), dataStr))

    part1()

    part2()
