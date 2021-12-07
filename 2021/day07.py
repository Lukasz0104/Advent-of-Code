from AoCUtils import readData
DAY = __file__[-5:-3]

def part1():
	# dataCopy = [x for x in data]
	
	fuelCost = -1

	for p in range(0, 1 + max(data)):
		s = 0
		for x in data:
			s += abs(x - p)
		if fuelCost == -1:
			fuelCost = s
		elif s < fuelCost:
			fuelCost = s

	print(f'solution to part 1: {fuelCost}')

def part2():
	
	fuelCost = -1

	for p in range(0, 1 + max(data)):
		s = 0
		for x in data:
			k = abs(x - p)
			s += k * (k+1) // 2
		if fuelCost == -1:
			fuelCost = s
		elif s < fuelCost:
			fuelCost = s

	print(f'solution to part 2: {fuelCost}')

if __name__ == '__main__':
	data = [int(x) for x in readData(DAY)[0].split(',')]

	part1()
	
	part2()