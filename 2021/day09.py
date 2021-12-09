from AoCUtils import readData
DAY = __file__[-5:-3]

from functools import reduce

def part1():
	res = 0

	SIZE_X = len(data)
	SIZE_Y = len(data[0])

	for row_index, row in enumerate(data):
		for column_index, value in enumerate(row):
			if row_index == 0:
				if column_index == 0: # top left corner
					if value < data[row_index+1][column_index] and value < data[row_index][column_index+1]:
						res += value + 1
				elif column_index == SIZE_Y - 1: # top right corner
					if value < data[row_index+1][column_index] and value < data[row_index][column_index - 1]:
						res += value + 1
				else: # top row
					if value < data[row_index+1][column_index] and value < data[row_index][column_index - 1] and value < data[row_index][column_index + 1]:
						res += value + 1
			elif row_index == SIZE_X - 1:
				if column_index == 0: # bottom left corner
					if value < data[row_index-1][column_index] and value < data[row_index][column_index+1]:
						res += value + 1
				elif column_index == SIZE_Y - 1: # bottom right corner
					if value < data[row_index-1][column_index] and value < data[row_index][column_index - 1]:
						res += value + 1
				else: # bottom row
					if value < data[row_index-1][column_index] and value < data[row_index][column_index - 1] and value < data[row_index][column_index + 1]:
						res += value + 1
			else:
				if column_index == 0: # left column
					if value < data[row_index + 1][column_index] and value < data[row_index - 1][column_index] and value < data[row_index][column_index + 1]:
						res += value + 1
				elif column_index == SIZE_Y - 1: # right column
					if value < data[row_index + 1][column_index] and value < data[row_index - 1][column_index] and value < data[row_index][column_index - 1]:
						res += value + 1
				else:
					if value < data[row_index+1][column_index] and value < data[row_index-1][column_index] and value < data[row_index][column_index+1] and value < data[row_index][column_index-1]:
						res += value + 1
	
	print(f'solution to part 1: {res}')

def basinSize(xPos, yPos, data) -> int:
	r = 0
	if data[xPos][yPos][0] != 9 and data[xPos][yPos][1] == False:
		data[xPos][yPos][1] = True
		r = 1
		if xPos != 0:
			r += basinSize(xPos - 1, yPos, data)
		if xPos != len(data) - 1:
			r += basinSize(xPos + 1, yPos, data)
		if yPos != 0:
			r += basinSize(xPos, yPos - 1, data)
		if yPos != len(data[0]) - 1:
			r += basinSize(xPos, yPos + 1, data)
	return r

def part2():
	dataCopy = [[[y, False] for y in x] for x in data]
	SIZE_X = len(data)
	SIZE_Y = len(data[0])
	sizes = []

	for row_index, row in enumerate(data):
		for column_index, value in enumerate(row):
			if row_index == 0:
				if column_index == 0: # top left corner
					if value < data[row_index+1][column_index] and value < data[row_index][column_index+1]:
						bS = basinSize(row_index, column_index, dataCopy)
						
						sizes.append(bS)
						sizes.sort(reverse=True)
						if len(sizes) > 3:
							sizes = sizes[:3]
						
				elif column_index == SIZE_Y - 1: # top right corner
					if value < data[row_index+1][column_index] and value < data[row_index][column_index - 1]:
						bS = basinSize(row_index, column_index, dataCopy)
						
						sizes.append(bS)
						sizes.sort(reverse=True)
						if len(sizes) > 3:
							sizes = sizes[:3]
						
				else: # top row
					if value < data[row_index+1][column_index] and value < data[row_index][column_index - 1] and value < data[row_index][column_index + 1]:
						bS = basinSize(row_index, column_index, dataCopy)
						
						sizes.append(bS)
						sizes.sort(reverse=True)
						if len(sizes) > 3:
							sizes = sizes[:3]
						
			elif row_index == SIZE_X - 1:
				if column_index == 0: # bottom left corner
					if value < data[row_index-1][column_index] and value < data[row_index][column_index+1]:
						bS = basinSize(row_index, column_index, dataCopy)
						
						sizes.append(bS)
						sizes.sort(reverse=True)
						if len(sizes) > 3:
							sizes = sizes[:3]
						
				elif column_index == SIZE_Y - 1: # bottom right corner
					if value < data[row_index-1][column_index] and value < data[row_index][column_index - 1]:
						bS = basinSize(row_index, column_index, dataCopy)
						
						sizes.append(bS)
						sizes.sort(reverse=True)
						if len(sizes) > 3:
							sizes = sizes[:3]
						
				else: # bottom row
					if value < data[row_index-1][column_index] and value < data[row_index][column_index - 1] and value < data[row_index][column_index + 1]:
						bS = basinSize(row_index, column_index, dataCopy)
						
						sizes.append(bS)
						sizes.sort(reverse=True)
						if len(sizes) > 3:
							sizes = sizes[:3]
						
			else:
				if column_index == 0: # left column
					if value < data[row_index + 1][column_index] and value < data[row_index - 1][column_index] and value < data[row_index][column_index + 1]:
						bS = basinSize(row_index, column_index, dataCopy)
						
						sizes.append(bS)
						sizes.sort(reverse=True)
						if len(sizes) > 3:
							sizes = sizes[:3]
						
				elif column_index == SIZE_Y - 1: # right column
					if value < data[row_index + 1][column_index] and value < data[row_index - 1][column_index] and value < data[row_index][column_index - 1]:
						bS = basinSize(row_index, column_index, dataCopy)
						
						sizes.append(bS)
						sizes.sort(reverse=True)
						if len(sizes) > 3:
							sizes = sizes[:3]
						
				else:
					if value < data[row_index+1][column_index] and value < data[row_index-1][column_index] and value < data[row_index][column_index+1] and value < data[row_index][column_index-1]:
						bS = basinSize(row_index, column_index, dataCopy)
						
						sizes.append(bS)
						sizes.sort(reverse=True)
						if len(sizes) > 3:
							sizes = sizes[:3]
	
	print(f'solution to part 2: {reduce(lambda x,y: x*y, sizes, 1)}')

if __name__ == '__main__':
	data = [tuple(map(int, x)) for x in readData(DAY)]
	
	part1()
	
	part2()