import urllib.request as req
import sys
from pathlib import Path


def readCookie():
	with open(f'{Path(__file__).parent}/cookie.txt','r') as f:
		return f.read()

def getInput(day: int) -> str:
	rq = req.Request(f'https://adventofcode.com/2021/day/{day}/input')
	rq.add_header("cookie", readCookie())
	res = req.urlopen(rq)
	return res.read().decode('utf-8')

if __name__ == "__main__":
	print(sys.argv)
	if len(sys.argv) < 2:
		print("Usage: python[.exe] DAY")
		sys.exit(-1)
	else:
		DAY = int(sys.argv[1])
	with open(f'{Path(__file__).parent}/{DAY if DAY > 9 else "0"+str(DAY)}.txt', 'w') as file:
		file.write(getInput(DAY))