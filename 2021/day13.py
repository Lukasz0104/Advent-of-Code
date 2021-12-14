from AoCUtils import readData
DAY = __file__[-5:-3]


def part1():
	grid = [['.' for x in range(dimX + 1)] for y in range(dimY + 1)]

	for point in points:
		x,y = point
		grid[y][x] = '#'

	axis, value = folds[0]

	gridCopy = [[x for x in y] for y in grid]


	if axis == 'x':
		for y in range(dimY + 1):
			for x in range(1, dimX + 1 - value):
				if gridCopy[y][value - x] == '#' or gridCopy[y][value + x] == '#':
					gridCopy[y][value - x] = '#' 
		for i,r in enumerate(gridCopy):
			grid[i] = r[:value]
	else: # axis == 'y'
		for y in range(1, dimY + 1 - value):
			for x in range(dimX + 1):
				gridCopy[value - y][x] = '#' if gridCopy[value - y][x] == '#' or gridCopy[value + y][x] == '#' else '.'
		grid = gridCopy[:value]
	

	res = 0
	for row in grid:
		for col in row:
			if col == '#':
				res += 1
	
	print(f'solution to part 1: {res}')


def part2():
	grid = [['.' for x in range(dimX + 1)] for y in range(dimY + 1)]

	for point in points:
		x,y = point
		grid[y][x] = '#'

	for fold in folds:
		axis, value = fold
		gridCopy = [[x for x in y] for y in grid]

		if axis == 'x':
			for y in range(len(gridCopy)):
				for x in range(1, len(gridCopy[0]) - value):
					if gridCopy[y][value - x] == '#' or gridCopy[y][value + x] == '#':
						gridCopy[y][value - x] = '#' 
			
			for i,r in enumerate(gridCopy):
				grid[i] = r[:value]
		
		else: # axis == 'y'
			for y in range(1, len(gridCopy) - value):
				for x in range(len(gridCopy[0])):
					if gridCopy[value - y][x] == '#' or gridCopy[value + y][x] == '#':
						gridCopy[value - y][x] = '#' 
			
			grid = gridCopy[:value]

	print('solution to part 2:')
	for row in grid:
		for col in row:
			if col == '.':
				print(' ',end='')
			else:
				print('#', end='')
		print()

if __name__ == '__main__':
	data = readData(DAY)

	points = []
	folds = []

	dimX = dimY = 0

	for line in data:
		if 'fold' in line:
			axis, val = line[11:].split('=')
			folds.append((axis, int(val)))
		elif line == '':
			continue
		else:
			x,y = line.split(',')
			x = int(x)
			y = int(y)
			dimX = max(dimX, x)
			dimY = max(dimY, y)
			points.append((x,y))

	part1()

	part2()
