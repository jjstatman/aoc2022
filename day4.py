import numpy as np

if __name__ == "__main__":
    
    with open("day4.txt") as f:
        data = [[(int(x.split('-')[0]),int(x.split('-')[1])) for x in line.split(',')] for line in f.read().split('\n') if line]
    sol1 = 0
    sol2 = 0
    for line in data:
        if (line[0][0] <= line[1][1] and line[0][1] >= line[1][0]) or (line[1][0] <= line[0][1] and line[1][1] >= line[0][0]):
            sol2 += 1
            if (line[0][0] >= line[1][0] and line[0][1] <= line[1][1]) or (line[1][0] >= line[0][0] and line[1][1] <= line[0][1]):
                sol1 += 1

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
