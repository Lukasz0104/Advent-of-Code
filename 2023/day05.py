import sys
from typing import List, Tuple
sys.path.append("..")

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


def part1():
    min_location = -1
    for seed in seeds:
        locationDest = get_location(seed)

        if min_location == -1 or locationDest < min_location:
            min_location = locationDest

    print(f"solution to part 1: {min_location}")


def get_destination(input_map: List[Tuple[int, int, int]], value: int) -> int:
    for (d, s, c) in input_map:
        if s <= value and value < s + c:
            return d + value - s
    return value


def get_location(seed: int) -> int:
    soilDest = get_destination(soil, seed)
    fertDest = get_destination(fertilizer, soilDest)
    waterDest = get_destination(water, fertDest)
    lightDest = get_destination(light, waterDest)
    temperatureDest = get_destination(temperature, lightDest)
    humidityDest = get_destination(humidity, temperatureDest)
    locationDest = get_destination(location, humidityDest)

    return locationDest


def part2():
    seed_pairs = [tuple([seeds[i], seeds[i + 1]]) for i in range(0, len(seeds), 2)]
    min_location = -1
    # Absolutely disgusting brute-force solution (finishes in <4h!)
    for (s, c) in seed_pairs:
        for i in range(c):
            l = get_location(s + i)
            if min_location == -1 or l < min_location:
                min_location = l

    print(f"solution to part 2: {min_location}")


def get_chunks() -> List[List[str]]:
    chunks = []
    current_chunk = []

    for item in dataStr:
        if item == "":
            chunks.append(current_chunk)
            current_chunk = []
        else:
            current_chunk.append(item)

    if len(current_chunk) > 0:
        chunks.append(current_chunk)

    return chunks


def parse_input() -> Tuple[List[int], List[Tuple[int, int, int]]]:
    chunks = get_chunks()

    seeds = list(map(int, chunks[0][0].replace("seeds: ", "").split()))

    maps = []

    for chunk in chunks[1:]:
        chunk = chunk[1:]  # omit first line with name
        maps.append([tuple(int(x) for x in line.split()) for line in chunk])

    return (seeds, maps)


if __name__ == "__main__":
    dataStr = readData(DAY, YEAR)

    seeds, (
        soil,
        fertilizer,
        water,
        light,
        temperature,
        humidity,
        location,
    ) = parse_input()
    part1()

    part2()
