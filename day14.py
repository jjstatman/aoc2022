import numpy as np
import copy
import json
from functools import cmp_to_key

if __name__ == "__main__":
    with open("day14.txt") as f:
        data = [[tuple(int(z) for z in y.split(',')) for y in x.split(' -> ')] for x in f.read().split("\n") if x]
    scan = {}
    ul = list(data[0][0])
    lr = list(data[0][0])

    for line in data:
        for i, corner in enumerate(line):
            scan[corner] = 0
            if i > 0:
                sec_len = max(abs(corner[0] - line[i-1][0]),abs(corner[1] - line[i-1][1]))
                direction = ((corner[0] - line[i-1][0])/sec_len, (corner[1] - line[i-1][1])/sec_len)
                for j in range(sec_len):
                    location = (line[i-1][0] + direction[0]*(j+1), line[i-1][1] + direction[1]*(j+1))
                    scan[location] = 0
            if corner[0] > lr[0]:
                lr[0] = corner[0]
            if corner[1] > lr[1]:
                lr[1] = corner[1]
            if corner[0] < ul[0]:
                ul[0] = corner[0]
            if corner[1] < ul[1]:
                ul[1] = corner[1]
    bottom = lr[1]
    sol1 = 0
    sands = 0
    while True:
        if (500, 0) in scan:
            break
        location = np.array([500,0])
        while True:
            if not tuple(location + [0,1]) in scan:
                if not sol1 and location[1] >= bottom:
                    sol1 = sands
                if location[1] > bottom:
                    scan[tuple(location)] = 1
                    sands += 1
                    break
                location = location + [0,1]
            elif not tuple(location + [-1,1]) in scan:
                location = location + [-1,1]
            elif not tuple(location + [1,1]) in scan:
                location = location + [1,1]
            else:
                scan[tuple(location)] = 1
                sands += 1
                break

    sol2 = sands

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
