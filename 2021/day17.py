from AoCUtils import readData
DAY = __file__[-5:-3]

def part1():
	minX = 0
	while minX * (minX + 1) // 2 < L1:
		minX += 1
	
	maxH = 0

	for vx in range(minX, L2):
		for vy in range(0, -H1):
			if willReach(vx, vy):
				if vy > 0:
					maxH = max(maxH, vy * (vy + 1) // 2)
	
	print(f'solution to part 1: {maxH}')

def willReach(v_x, v_y):
	pX = pY = 0
	while True:
		pX += v_x
		pY += v_y
		
		v_y -= 1
		v_x = max(v_x - 1, 0)

		if L1 <= pX and pX <= L2 and H1 <= pY and pY <= H2:
			return True
		if pX > L2 or pY < H1:
			return False

def part2():
	minX = 0

	while minX * (minX + 1) // 2 < L1:
		minX += 1

	count = 0

	for vx in range(minX, L2 + 1):
		for vy in range(H1, -H1):
			if willReach(vx, vy):
				count += 1
	
	print(f'solution to part 2: {count}')

if __name__ == '__main__':
	data = readData(DAY)[0][13:].split(', ')

	L1, L2 = tuple(int(x) for x in data[0][2:].split('..'))
	H1, H2 = tuple(int(x) for x in data[1][2:].split('..'))
	
	part1()
	
	part2()