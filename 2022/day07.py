import sys
from typing import List
sys.path.append('..')

from AoCUtils import readData
DAY = __file__[-5:-3]
YEAR = __file__[-13:-9]


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self) -> str:
        return f'File(name={self.name}; size={self.size})'


class Dir:
    def __init__(self, name):
        self.name = name
        self.files: List[File] = []
        self.dirs = dict()

    def size(self):
        return sum(map(lambda d: d.size(), self.dirs.values())) + sum(map(lambda f: f.size, self.files))

    def __repr__(self) -> str:
        return f'Directory(name={self.name}; dirs={self.dirs}; files={self.files})'


def part1():
    res = sum(
        map(lambda x: x.size(), 
        filter(
            lambda d: d.size() < 100000, 
            fileSystem.values())))

    print(f'solution to part 1: {res}')


def part2():
    total_space = 70000000
    required_space = 30000000
    currently_used = fileSystem['/'].size()
    currently_free = total_space - currently_used

    deleted_size = sorted(
        filter(
            lambda d: d.size() + currently_free >= required_space, 
            fileSystem.values()), 
        key=lambda d: d.size())[0].size()

    print(f'solution to part 2: {deleted_size}')


if __name__ == '__main__':
    dataStr = readData(DAY, YEAR)

    fileSystem = {
        '/': Dir('/')
    }
    currentDir = '/'

    lineIndex = 1
    while lineIndex < len(dataStr):
        line = dataStr[lineIndex]
        tokens = line.split(' ')
        lineIndex += 1

        match tokens[1]:
            case 'cd':
                if tokens[2] == '..':
                    index = currentDir.rfind('/')
                    currentDir = currentDir[:index]
                    if currentDir == '':
                        currentDir = '/'
                else:
                    currentDir = (currentDir + '/' + tokens[2]).replace('//', '/')
            case 'ls':
                while lineIndex < len(dataStr) and not (line := dataStr[lineIndex]).startswith('$'):
                    tokens = line.split(' ')
                    name = tokens[1]
                    if tokens[0] == 'dir':
                        directory = Dir(name)
                        fileSystem[currentDir].dirs[directory.name] = directory
                        path = (currentDir + '/' + directory.name).replace('//', '/')
                        fileSystem[path] = directory
                    else:
                        size = int(tokens[0])
                        fileSystem[currentDir].files.append(File(name, size))
                    lineIndex += 1

    part1()

    part2()
