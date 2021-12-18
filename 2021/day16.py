from AoCUtils import readData
DAY = __file__[-5:-3]

from functools import reduce

'''
def extractPackets(i, packets):
	currentPacket = ""
	version = dataBinary[i : i + 3]
	i += 3

	typeID = dataBinary[i: i + 3]
	i += 3

	currentPacket += version
	currentPacket += typeID

	if typeID == "100":
		group = dataBinary[i : i + 5]
		currentPacket += group
		while group[0] != '0':
			group = dataBinary[i : i + 5]
			currentPacket += group
		packets.append(currentPacket)
		
		return currentPacket

	else:
		lengthTypeID = dataBinary[i]
		i += 1

		currentPacket += lengthTypeID

		if lengthTypeID == '0':
			subpacketsLength = dataBinary[i : i + 15]
			i += 15

			currentPacket += subpacketsLength

			spLength = int(subpacketsLength, 2)
			k = 0
			while k < spLength: 
				rest = extractPackets(i + k, packets)
				k += len(rest)
				currentPacket += rest
			packets.append(currentPacket)
			return currentPacket
		else:
			subPacketNumber = dataBinary[i : i + 11]
			i += 11

			currentPacket += subPacketNumber
			
			spN = int(subPacketNumber, 2)
			k = 0
			for _ in range(spN):
				sp = extractPackets(i + k, packets)
				currentPacket += sp
				k += len(sp)
			
			packets.append(currentPacket)
			return currentPacket
'''

versionSum = 0

def extractPacketVersion(start : int):
	global versionSum
	i = start
	version = int(dataBinary[i : i+3], 2)
	typeID = int(dataBinary[i+3 : i+6], 2)
	i += 6

	versionSum += version
	if typeID == 4:
		group = dataBinary[i : i+5]
		i += 5
		while group[0] == '1':
			group = dataBinary[i : i+5]
			i += 5
		return i - start
	else:
		LTID = dataBinary[i]
		i += 1
		if LTID == '0':
			spL = int(dataBinary[i : i+15], 2)
			i += 15
			k = 0
			while k < spL:
				k += extractPacketVersion(i + k)
			# i += k
			return i + k - start
		else:
			spN = int(dataBinary[i : i+11], 2)
			i += 11
			k = 0
			for _ in range(spN):
				k += extractPacketVersion(i + k)
			return i + k - start

def part1():
	extractPacketVersion(0)

	print(f'solution to part 1: {versionSum}')

def processPackets(start : int):
	i = start
	typeID = int(dataBinary[i+3 : i+6], 2)
	i += 6

	if typeID == 4:
		group = dataBinary[i : i+5]
		i += 5
		value = group[1:]
		while group[0] == '1':
			group = dataBinary[i : i+5]
			value += group[1:]
			i += 5
		return i - start, int(value, 2)
	else:
		values = []
		LTID = dataBinary[i]
		i += 1
		k = 0
		if LTID == '0':
			spL = int(dataBinary[i : i+15], 2)
			i += 15
			while k < spL:
				k1, v = processPackets(i + k)
				k += k1
				values.append(v)
		else:
			spN = int(dataBinary[i : i+11], 2)
			i += 11
			for _ in range(spN):
				k1, v = processPackets(i + k)
				k += k1
				values.append(v)
		
		ind = i + k - start
		if typeID == 0:
			return ind, sum(values)
		elif typeID == 1:
			return ind, reduce(lambda x, y: x*y, values, 1)
		elif typeID == 2:
			return ind, min(values)
		elif typeID == 3:
			return ind, max(values)
		elif typeID == 5:
			x = 1 if values[0] > values[1] else 0
			return ind, x
		elif typeID == 6:
			x = 1 if values[0] < values[1] else 0
			return ind, x
		elif typeID == 7:
			x = 1 if values[0] == values[1] else 0
			return ind, x

def part2():
	print(f'solution to part 2: {processPackets(0)[1]}')

if __name__ == '__main__':
	data = readData(DAY)[0]
	dataBinary = "".join('0'*(4-len(bin(int(x,16))[2:])) + bin(int(x,16))[2:] for x in data)

	part1()
	
	part2()