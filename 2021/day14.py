from AoCUtils import readData
DAY = __file__[-5:-3]

def part1():
	# Initial idea, way too slow for part 2
	template = polymer_template
	
	counts = {x : polymer_template.count(x) for x in uniqueLetters}

	for step in range(10):
		templateList = list(template)
		inserts = []
		for insertion in insertions:
			pattern, new = insertion
			index = template.find(pattern)
			while index != -1:
				inserts.append((index + 1, new))
				index = template.find(pattern, index + 1)
		inserts.sort(key=lambda x : x[0])
		c = 0
		for ins in inserts:
			pos, val = ins
			templateList.insert(pos + c, val)
			counts[val] += 1
			c += 1
		template = ''.join(templateList)

	print(f'solution to part 1: {max(counts.values()) - min(counts.values())}')

def part2():
	pairs = {f'{x}{y}' : polymer_template.count(f'{x}{y}') for x in uniqueLetters for y in uniqueLetters}

	for step in range(40):
		pairsCopy = {x : pairs[x] for x in pairs}

		for insertion in insertions:
			pattern, new = insertion
			p1, p2 = tuple(pattern)
			t = pairs[pattern]

			s1 = p1 + new
			s2 = new + p2

			if t > 0:
				pairsCopy[pattern] -= t
				pairsCopy[s1] += t
				pairsCopy[s2] += t
		
		pairs = pairsCopy

	X = {letter : sum(pairs[x] for x in pairs if x[1] == letter) for letter in uniqueLetters}
	X[polymer_template[0]] += 1

	print(f'solution to part 2: {max(X.values()) - min(X.values())}')

if __name__ == '__main__':
	data = readData(DAY)

	polymer_template = data[0]
	insertions = []
	uniqueLetters = set()

	for line in data[2:]:
		p,n = line.split(' -> ')
		uniqueLetters.add(p[0])
		uniqueLetters.add(p[1])
		uniqueLetters.add(n)

		insertions.append((p, n))
	
	part1()

	part2()