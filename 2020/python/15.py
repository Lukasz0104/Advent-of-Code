
inp = list(map(int, input().split(',')))

def part1():
    said = [i for i in inp]
    for _ in range(len(inp),2020):
        if said[-1] not in said[:-1]:
            said.append(0)
        else:
            said.append(said[:-1][::-1].index(said[-1])+1)
    print(said[-1])

def part2():
    said = {inp[i]:i for i in range(len(inp))}
    next = 0
    for i in range(len(said),30000000):
        if next in said.keys():
            n = i - said[next]
            said[next] = i
            next = n
        else:
            said[next] = i
            next = 0
        
    print([k for k in said if said[k]==29999999][0])
    
part1()
part2()