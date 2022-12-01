#!/usr/bin/env python3
import urllib.request as req
import sys
from pathlib import Path
from datetime import date


def readCookie():
    with open(f'{Path(__file__).parent}/cookie.txt', 'r') as f:
        return f.read()


def getInput(day, year) -> str:
    rq = req.Request(f'https://adventofcode.com/{year}/day/{day}/input')
    rq.add_header("cookie", readCookie())
    res = req.urlopen(rq)
    return res.read().decode('utf-8')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python[.exe] getPuzzleData.py DAY [YEAR]")
        sys.exit(-1)
    elif len(sys.argv) == 2:
        DAY = sys.argv[1]
        YEAR = date.today().year
    elif len(sys.argv) == 3:
        DAY = sys.argv[1]
        YEAR = sys.argv[2]

    with open(f'{Path(__file__).parent}/{YEAR}/inputs/{"0" if len(DAY) == 1 else ""}{DAY}.txt', 'w') as file:
        file.write(getInput(DAY, YEAR))
