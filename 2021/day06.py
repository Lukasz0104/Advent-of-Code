from AoCUtils import readData
DAY = __file__[-5:-3]

def part1():
	dataCopy = [x for x in data]

	for day in range(80):
		N = 0
		for i,v in enumerate(dataCopy):
			if v == 0:
				N += 1
				dataCopy[i] = 6
			else:
				dataCopy[i] -= 1
		for _ in range(N):
			dataCopy.append(8)

	print(f'solution to part 1: {len(dataCopy)}')

def part2():
	dataCopy = [x for x in data]

	populations = {x : 0 for x in range(9)}

	for d in dataCopy:
		populations[d] += 1
	
	for i in range(256):
		k = populations[0]
		populations[0] = populations[1]
		populations[1] = populations[2]
		populations[2] = populations[3]
		populations[3] = populations[4]
		populations[4] = populations[5]
		populations[5] = populations[6]
		populations[6] = populations[7] + k
		populations[7] = populations[8]
		populations[8] = k
	
	print(f'solution to part 2: {sum(populations.values())}')

if __name__ == '__main__':
	data = [int(x) for x in readData(DAY)[0].split(',')]
	
	part1()
	
	part2()