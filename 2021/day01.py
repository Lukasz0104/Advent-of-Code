from readData import readData

def part1():
	previous = data[0]
	count = 0
	for current in data[1:]:
		if current > previous:
			count += 1
		previous = current
	
	print("solution to part 1:", count)

def part2():
	previous = data[0] + data[1] + data[2]
	count = 0
	for index in range(len(data[3:])):
		current = data[index] + data[index - 1] + data[index - 2]
		if current > previous:
			count += 1
		previous = current
	
	print("solution to part 2:", count)

if __name__ == "__main__":
	data = [int(x) for x in readData(1)]

	part1()

	part2()
