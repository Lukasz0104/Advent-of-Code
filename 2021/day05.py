from AoCUtils import readData, RED, GREEN, RESET
DAY = __file__[-5:-3]

class XYPlane:
	def __init__(self, N : int):
		self.N = N
		self.grid = [[0 for _ in range(N+1)] for _ in range(N+1)]
	
	def drawLine(self, x1, y1, x2, y2):
		if x1==x2 or y1==y2:
			x1,x2 = min(x1,x2), max(x1,x2)
			y1,y2 = min(y1,y2), max(y1,y2)
			for i in range(y1, y2+1):
				for j in range(x1, x2+1):
					self.grid[i][j] += 1
		
		else:
			if x1 > x2:
				x1, x2 = x2, x1
				y1, y2 = y2, y1
			
			D = abs(x1 - x2)
			dirY = 1 if y1<y2 else -1

			for d in range(D+1):
				self.grid[y1 + dirY * d][x1 + d] += 1


	def count(self) -> int:
		count = 0
		for row in self.grid:
			for col in row:
				if col > 1:
					count+=1
		return count

	def print(self):
		for row in self.grid:
			for col in row:
				print(f'{RED if col==0 else GREEN}{col:2}{RESET} ', end="")
			print()
		print()

def part1():
	xyPlane = XYPlane(N)

	for line in data:
		if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
			x1,y1 = line[0]
			x2,y2 = line[1]
			xyPlane.drawLine(x1,y1,x2,y2)

	print(f'solution to part 1: {xyPlane.count()}')

def part2():
	xyPlane = XYPlane(N)

	for line in data:
		x1,y1 = line[0]
		x2,y2 = line[1]
		xyPlane.drawLine(x1,y1,x2,y2)
	
	print(f'solution to part 2: {xyPlane.count()}')

if __name__ == '__main__':
	inp = [x.split(' -> ') for x in readData(DAY)]
	
	data = []

	for line in inp:
		points = []
		for p in line:
			points.append(tuple(map(int, p.split(','))))
		data.append(tuple(points))

	N = 0
	for line in data:
		x1,y1 = line[0]
		x2,y2 = line[1]
		N = max(N,x1,y1,x2,y2)
	
	part1()
	
	part2()