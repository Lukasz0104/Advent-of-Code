def result(value, mask) -> int:
    v = bin(value)[2:]
    while len(v)<36:
        v = '0'+v
    v = list(v)
    for i in range(36):
        if mask[i]=='0':
            v[i]='0'
        elif mask[i]=='1':
            v[i]='1'
    return int(''.join(v),2)

def memory(value, mask):
    v = bin(value)[2:]
    while len(v)<36:
        v = '0' + v
    v = list(v)
    for i in range(36):
        if mask[i]=='0':
            continue
        elif mask[1]=='1':
            v[i]='1'
        else:
            v[i]='X'
    print(''.join(v))
    return ''.join(v)

def floating(mem):
    d = []
    mem = list(mem)
    for i in range(len(mem)):
        if mem[i]=='X':
            for j in range(2):
                mem[i] = str(j)
                d.extend(floating(mem))
    return d

inp = []
s = input()
while (len(s)>0):
    s1, s2 = s.split(" = ")
    if s1=='mask':
        inp.append((s1,s2))
    else:
        inp.append((s1[4:-1],s2))
    try:
        s = input()
    except:
        break


def part1():
    d = {}
    mask = ''
    for line in inp:
        if line[0]=='mask':
            mask = line[1]
        else:
            d[int(line[0])]=result(int(line[1]), mask)
    
    for i in sorted(d.keys()):
        print(i,":",d[i])

    print(sum([d[i] for i in d]))

def part2():
    #d = {}
    mask = ''
    for line in inp:
        if line[0]=='mask':
            mask = line[1]
        else:
            v = int(line[1])
            mem = memory(v, mask)
            print(mem)
            print(floating(mem))

#memory(42,"000000000000000000000000000000X1001X")


part1()
#part2()
#'''