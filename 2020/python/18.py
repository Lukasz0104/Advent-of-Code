with open(".\\..\\in\\18.txt") as inputFile:
    INPUT = []
    #[[x in line.split(' ') if '(' not in x and ')' not in x else ] for line in inputFile.read().split('\n')]
    for line in inputFile.read().split('\n'):
        temp = []
        for x in line.split(' '):
            if '(' in x:
                temp.append('(')
                temp.append(x)
            elif ')' in x:
                temp.append(')')
                temp.append(x)
            else:
                temp.append(x)
        #print(temp)
        INPUT.append(temp)

def evaluateLine(line) -> int:    
    new_line = []

    number1 = 0
    number2 = 0
    operation = ''
    
    while (len(line)>2):
        pass

    return line[0]



print(INPUT[0])

evaluateLine("1 + 2 * 3 + 4 * 5 + 6")
evaluateLine("1 + (2 * 3) + (4 * (5 + 6))")