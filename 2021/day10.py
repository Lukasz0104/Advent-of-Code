from AoCUtils import readData
DAY = __file__[-5:-3]

from collections import deque

def part1():
	s = 0
	for line in data:
		queue = deque()
		for ch in line:
			if ch in "([{<":
				queue.append(ch)
			else:
				if ch == ')' and queue[-1] == "(" or queue[-1] == chr(ord(ch) - 2):
					queue.pop()
				else:
					if ch == ')':
						s += 3
					elif ch == "]":
						s += 57
					elif ch == '}':
						s += 1197
					else:
						s += 25137
					break
	
	print(f'solution to part 1: {s}')

def part2():
	scores = []
	for line in data:
		queue = deque()
		for ch in line:
			if ch in "([{<":
				queue.append(ch)
			else:
				if ch == ')' and queue[-1] == "(" or queue[-1] == chr(ord(ch) - 2):
					queue.pop()
				else:
					break
		else:
			s1 = 0
			queue.reverse()
			for d in queue:
				s1 *= 5
				if d == '(':
					s1 += 1
				elif d == '[':
					s1 += 2
				elif d == '{':
					s1 += 3
				else:
					s1 += 4
			scores.append(s1)
	
	scores.sort()

	print(f'solution to part 2: {scores[len(scores) // 2]}')

if __name__ == '__main__':
	data = readData(DAY)

	part1()
	
	part2()