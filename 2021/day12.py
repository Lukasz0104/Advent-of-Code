from AoCUtils import readData
DAY = __file__[-5:-3]

def traverse1(connections, visited, current, foundRoutes):
	if current == 'end' and visited not in foundRoutes:
		foundRoutes.append(visited)
		return 1
	
	s = 0

	for conn in connections[current]:
		if conn == 'start': continue
		if conn.islower() and visited.count(conn) > 0:
			continue
		visitedCopy = [v for v in visited]
		visitedCopy.append(conn)
		s += traverse1(connections, visitedCopy, conn, foundRoutes)

	return s

def traverse2(connections, visited, current, foundRoutes):
	if current == 'end' and visited not in foundRoutes:
		foundRoutes.append(visited)
		return 1
	
	s = 0

	for conn in connections[current]:
		if conn == 'start': 
			continue

		if conn.islower():
			maxCount = 0
			for v in visited:
				if v.islower():
					maxCount = max(maxCount, visited.count(v))
			if maxCount == 2 and visited.count(conn) > 0:
				continue

		visitedCopy = [v for v in visited]
		visitedCopy.append(conn)
		s += traverse2(connections, visitedCopy, conn, foundRoutes)
	
	return s

def part1():
	nodes = set([x[0] for x in data] + [x[1] for x in data])

	connections = {node : set() for node in nodes}

	for conn in data:
		x,y = conn
		connections[x].add(y)
		connections[y].add(x)
		
	r = traverse1(connections, [], 'start', [])

	print(f'solution to part 1: {r}')

def part2():
	nodes = set([x[0] for x in data] + [x[1] for x in data])

	connections = {node : set() for node in nodes}

	for conn in data:
		x,y = conn
		connections[x].add(y)
		connections[y].add(x)
	
	r = traverse2(connections, [], 'start', [])
	
	print(f'solution to part 2: {r}')

if __name__ == '__main__':
	data = [tuple(x.split('-')) for x in readData(DAY)]
	
	part1()
	
	part2()