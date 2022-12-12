import numpy as np
import copy

if __name__ == "__main__":
    with open("day12.txt") as f:
        data = np.array([[ord(c) - ord('a') for c in x] for x in f.read().split("\n") if x])
    steps = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            steps[(i,j)] = -1
            if data[i,j] == ord('S')-ord('a'):
                start = (i,j)
                data[i,j] = 0
            elif data[i,j] == ord('E')-ord('a'):
                end = (i,j)
                data[i,j] = 25
    lastlocs = [end]
    steps[end] = 0
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    nextlocs = []
    sol2 = -1
    while steps[start] < 0:
        for loc in lastlocs:
            for d in dirs:
                check = tuple(sum(x) for x in zip(loc,d))
                if check[0] >= 0 and check[0] < len(data) and check[1] >= 0 and check[1] < len(data[0]):
                    if steps[check] < 0 and data[check] >= data[loc] - 1:
                        steps[check] = steps[loc] + 1
                        nextlocs.append(check)
                        if sol2 < 0 and data[check] == 0:
                            sol2 = steps[check]
        lastlocs = nextlocs
        nextlocs = []

    sol1 = steps[start]

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
