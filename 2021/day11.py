from AoCUtils import readData
DAY = __file__[-5:-3]

def part1():
	flashCount = 0

	dataCopy = [[x for x in y] for y in data]

	STEPS = 100

	for _ in range(STEPS):
		flashed_this_step = []
		flashedFlag = True
		for r in range(10):
			for c in range(10):
				dataCopy[r][c] += 1

		while flashedFlag:
			flashedFlag = False
			for r in range(10):
				for c in range(10):
					if dataCopy[r][c] > 9 and [r,c] not in flashed_this_step:
						flashed_this_step.append([r,c])
						for dr in [-1,0,1]:
							if dr == -1 and r == 0:
								continue
							if dr == 1 and r == 9:
								continue
							for dc in [-1,0,1]:
								if dr == dc and dr == 0:
									continue
								if dc == -1 and c == 0:
									continue
								if dc == 1 and c == 9:
									continue
								dataCopy[r+dr][c+dc] += 1
								if dataCopy[r+dr][c+dc] > 9:
									flashedFlag = True
		
		for r in range(10):
			for c in range(10):
				if dataCopy[r][c] > 9:
					dataCopy[r][c] = 0
					flashCount += 1

	print(f'solution to part 1: {flashCount}')

def printCavern(data):
	for r in data:
		print(r)
	print()

def part2():
	dataCopy = [[x for x in y] for y in data]

	step = 0

	while any([any(x != 0 for x in y) for y in dataCopy]):
		flashed_this_step = []
		flashedFlag = True
		for r in range(10):
			for c in range(10):
				dataCopy[r][c] += 1

		while flashedFlag:
			flashedFlag = False
			for r in range(10):
				for c in range(10):
					if dataCopy[r][c] > 9 and [r,c] not in flashed_this_step:
						flashed_this_step.append([r,c])
						for dr in [-1,0,1]:
							if dr == -1 and r == 0:
								continue
							if dr == 1 and r == 9:
								continue
							for dc in [-1,0,1]:
								if dr == dc and dr == 0:
									continue
								if dc == -1 and c == 0:
									continue
								if dc == 1 and c == 9:
									continue
								dataCopy[r+dr][c+dc] += 1
								if dataCopy[r+dr][c+dc] > 9:
									flashedFlag = True

		for r in range(10):
			for c in range(10):
				if dataCopy[r][c] > 9:
					dataCopy[r][c] = 0
		
		step += 1
	
	print(f'solution to part 2: {step}')

if __name__ == '__main__':
	data = [[int(x) for x in y] for y in readData(DAY)]

	part1()
	
	part2()