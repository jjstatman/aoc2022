import numpy as np
import copy
import json
from functools import cmp_to_key

if __name__ == "__main__":
    with open("day18.txt") as f:
        data = np.array([[int(y) for y in x.split(',')] for x in f.read().split('\n')])
    neighbors = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
    cubemin = np.min(data,axis=0)
    cubes = {}
    sol1 = 0
    sol2 = 0
    start = []
    for cube in data:
        num_adj = 0
        if not len(start) and cube[0] == cubemin[0]:
            start = cube
        for neighbor in neighbors:
            test = tuple(cube + neighbor)
            if test in cubes:
                num_adj += 1
        cubes[tuple(cube)] = 1
        sol1 += 6 - num_adj*2
    start = start - [1,0,0]
    waterlayer = {}
    last_check = [(start,0)]
    while True:
        next_check = set([])
        for check, it in last_check:
            if tuple(check) in waterlayer:
                continue
            waterlayer[tuple(check)] = 1
            num_adj = 0
            to_test = set([])
            for neighbor in neighbors:
                test = tuple(check + neighbor)
                if not test in waterlayer:
                    if test in cubes:
                        num_adj += 1
                    else:
                        to_test.add(test)
            if num_adj > 0:
                for next_test in to_test:
                    next_check.add((next_test,0))
                sol2 += num_adj
            if num_adj == 0 and it < 1:
                for next_test in to_test:
                    next_check.add((next_test,it+1))
        last_check = copy.deepcopy(next_check)
        if not len(last_check):
            break

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
