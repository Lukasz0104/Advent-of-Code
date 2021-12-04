from typing import Tuple
from AoCUtils import readData, GREEN, RED, RESET
from copy import deepcopy
DAY = __file__[-5:-3]

class BingoElement:
	def __init__(self, num):
		self.num = num
		self.marked = False


class BingoBoard:
	def __init__(self, bingo):
		self.board = [[BingoElement(x) for x in row] for row in bingo]

	def print(self):
		for r in self.board:
			for c in r:
				print(f'{GREEN if c.marked else RED}{c.num:2}{RESET}',end=" ")
			print("")
	
	def mark(self, value):
		for row in self.board:
			for e in row:
				if e.num == value:
					e.marked = True
					return self.isWinning()
		return False

	def isWinning(self) -> bool:
		for i in range(5):
			isRowWinning = isColumnWinning = True
			for j in range(5):
				isRowWinning &= self.board[i][j].marked
				isColumnWinning &= self.board[j][i].marked

			if isRowWinning or isColumnWinning:
				return True
		return False

	def getUnmarked(self):
		unmarked = []
		for r in self.board:
			for c in r:
				if not(c.marked):
					unmarked.append(c.num)
		return unmarked


def part1():
	boardsCopy = deepcopy(bingoBoards)
	res = 0
	flag = False
	for num in numbers:
		for board in boardsCopy:
			if flag:
				break
			if board.mark(num):
				res = sum(board.getUnmarked()) * num
				flag = True
				break
		if flag:
			break

	print(f'solution to part 1: {res}')


def part2():
	boardsCopy = deepcopy(bingoBoards)
	res = 0

	for number in numbers:
		for board in boardsCopy:
			board.mark(number)

		if len(boardsCopy) > 1:
			boardsCopy = list(filter(lambda x : not(x.isWinning()), boardsCopy))
		else:
			res = sum(boardsCopy[0].getUnmarked()) * number
			break
		
	print(f'solution to part 2: {res}')


if __name__ == '__main__':
	data = readData(DAY)
	numbers = list(map(int, data[0].split(',')))

	bingoBoards = []
	for i in range(1, len(data), 6):
		bingo = []
		for d in range(1, 6):
			bingo.append(
				list(map(int, data[i+d].lstrip().replace('  ', ' ').split(' '))))
		bingoBoards.append(BingoBoard(bingo))

	part1()

	part2()
