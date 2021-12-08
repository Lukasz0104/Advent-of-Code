from AoCUtils import readData
DAY = __file__[-5:-3]

def part1():
	r = 0

	for d in data:
		for x in d[1]:
			if len(x) in [2,3,4,7]:
				r += 1
	
	print(f'solution to part 1: {r}')

def part2():
	Sum = 0

	UP = 0
	LEFT_UP = 1
	RIGHT_UP = 2
	MID = 3
	LEFT_DOWN = 4
	RIGHT_DOWN = 5
	DOWN = 6

	DIGITS = [
		[UP,LEFT_UP,RIGHT_UP,LEFT_DOWN,RIGHT_DOWN,DOWN],
		[RIGHT_UP,RIGHT_DOWN],
		[UP,RIGHT_UP,MID,LEFT_DOWN,DOWN],
		[UP,RIGHT_UP,MID,RIGHT_DOWN,DOWN],
		[LEFT_UP,RIGHT_UP,MID,RIGHT_DOWN],
		[UP,LEFT_UP,MID,RIGHT_DOWN,DOWN],
		[UP,LEFT_UP,MID,LEFT_DOWN,RIGHT_DOWN,DOWN],
		[UP,RIGHT_UP,RIGHT_DOWN],
		[UP,LEFT_UP,RIGHT_UP,MID,LEFT_DOWN,RIGHT_DOWN,DOWN],
		[UP,LEFT_UP,RIGHT_UP,MID,RIGHT_DOWN,DOWN]]


	for d1 in data:
		D = {x : [] for x in range(7)}

		sortedD1 = sorted([x for x in d1[0]], key=len)
		
		'''
		we start with figuring out what symbols will be in RIGHT_UP and RIGHT_DOWN panels
		'''
		D[RIGHT_UP] = D[RIGHT_DOWN] = list(sortedD1[0])
		
		'''
		then figure out the top panel
		it is the symbol for 7, that is not present among symbols for 1
		'''
		D[UP] = [x for x in sortedD1[1] if x not in sortedD1[0]]

		'''
		then we can limit possibilites for LEFT_UP and MID to just to two symbols in the following way:
		we select symbols used for 4 that were not used for 1'''
		D[LEFT_UP] = D[MID] = [x for x in sortedD1[2] if x not in sortedD1[0]]
		
		'''
		now we filter out symbols that are missing in sequences of length 6
		'''
		differences = [x for x in sortedD1[-1] if any([x not in y for y in sortedD1[6:9]])] 

		'''symbol for RIGHT_UP is such from the differences that was previously an option in RIGHT_UP'''
		D[RIGHT_UP] = [x for x in differences if x in D[RIGHT_UP]]

		'''symbol for RIGHT_DOWN is the other option'''
		D[RIGHT_DOWN] = [x for x in D[RIGHT_DOWN] if x not in D[RIGHT_UP]]

		'''now we determine MID in a similar way to RIGHT_UP'''
		D[MID] = [x for x in differences if x in D[MID]]
		
		'''similar to RIGHT_DOWN'''
		D[LEFT_UP] = [x for x in D[LEFT_UP] if x not in D[MID]]

		'''the last one from differences'''
		D[LEFT_DOWN] = [x for x in differences if x not in D[MID] and x not in D[RIGHT_UP]]
		
		'''the last one that was not used'''
		D[DOWN] = [x for x in sortedD1[-1] if all([x not in D[y] for y in range(6)])]
		
		SYMBOL_TO_POSITION = {D[k][0] : k for k in D}
		
		s = 0

		for digit in d1[1]:
			p = sorted([SYMBOL_TO_POSITION[x] for x in digit])
			s = 10*s + DIGITS.index(p)

		Sum += s

	print(f'solution to part 2: {Sum}')

if __name__ == '__main__':
	data = [[x.split(' | ')[0].split(' '), x.split(' | ')[1].split(' ')] 
				for x in readData(DAY)]
	
	part1()
	
	part2()