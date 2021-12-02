from pathlib import Path

def readData(day: int):
	with open(f'{Path(__file__).parent}/inputs/{day}.txt') as file:
		return file.read().split('\n')[:-1]