from AoCUtils import readData
DAY = __file__[-5:-3]


def part1():
    LEN = len(data[0])
    g = e = '0b'

    for l in range(LEN):
        count0 = count1 = 0
        for d in data:
            if d[l] == '1':
                count1 += 1
            else:
                count0 += 1

        if count1 > count0:
            g = g + '1'
            e = e + '0'
        else:
            g = g + '0'
            e = e + '1'

    print(f'solution to part 1: {int(g,2) * int(e,2)}')


def part2():
    LEN = len(data[0])

    oxygenDataCopy = [x for x in data]
    co2DataCopy = [x for x in data]

    for j in range(LEN):
        count0 = count1 = 0
        for d in oxygenDataCopy:
            if d[j] == '1':
                count1 += 1
            else:
                count0 += 1

        if count1 == count0 and len(oxygenDataCopy) > 1:
            oxygenDataCopy = list(
                filter(lambda x: x[j] == '1', oxygenDataCopy))
        elif count1 > count0 and len(oxygenDataCopy) > 1:
            oxygenDataCopy = list(
                filter(lambda x: x[j] == '1', oxygenDataCopy))
        elif len(oxygenDataCopy) > 1:
            oxygenDataCopy = list(
                filter(lambda x: x[j] == '0', oxygenDataCopy))

        count0 = 0
        count1 = 0
        for d in co2DataCopy:
            if d[j] == '1':
                count1 += 1
            else:
                count0 += 1

        if count1 == count0 and len(co2DataCopy) > 1:
            co2DataCopy = list(filter(lambda x: x[j] == '0', co2DataCopy))
        elif count1 > count0 and len(co2DataCopy) > 1:
            co2DataCopy = list(filter(lambda x: x[j] == '0', co2DataCopy))
        elif len(co2DataCopy) > 1:
            co2DataCopy = list(filter(lambda x: x[j] == '1', co2DataCopy))

    x, y = int('0b'+oxygenDataCopy[0], 2), int('0b'+co2DataCopy[0], 2)

    print(f'solution to part 2: {x * y}')


if __name__ == '__main__':
    data = readData(DAY)
    # data = ['00100', '11110', '10110', '10111', '10101', '01111',
    #         '00111', '11100', '10000', '11001', '00010', '01010']

    part1()

    part2()
