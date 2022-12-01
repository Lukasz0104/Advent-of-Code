from pathlib import Path
from datetime import date

GREEN = chr(27) + "[92m"
RESET = chr(27) + "[0m"
RED = chr(27) + "[91m"

def readData(day, year):
    with open(f'{Path(__file__).parent}/{year}/inputs/{day}.txt') as file:
        return file.read().split('\n')[:-1]
