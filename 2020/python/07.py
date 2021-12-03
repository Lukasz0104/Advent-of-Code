import re
from pathlib import Path

def processInput():
    inp = {}
    with open(f"D:\\repos\\AoC\\2020\\in\\{__file__[-5:-3]}.txt") as f:
        for line in f.read().split('\n'):
            if line=='':
                continue
            x = re.findall(r"no other bags|\d+ (\w+ \w+) bag[s, ]*",line)
            if x == ['']:
                x = []
            inp[re.findall(r"^\w+ \w+",line)[0]] = x
    return inp

c1 = 0

def traverse(graph, node, visited = set()):
    if node in visited:
        return 0
    visited.add(node)
    numBagColors = 1
    for N in graph[node]:
        numBagColors += traverse(graph,N,visited)
    return numBagColors

def part1():
    graph = {}
    
    for k,v in inp.items():
        if not k in graph:
            graph[k]=[]
        for src in v:
            if not src in graph:
                graph[src] = []
            graph[src].append(k)
    
    print(traverse(graph,"shiny gold") - 1)

def part2():
    pass





inp = processInput()
part1()
part2()