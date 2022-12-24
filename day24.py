import numpy as np
import copy
import json
from functools import cmp_to_key

def get_next_checks(mymap,cur_loc,cur_time,modulo):
    directions = np.array([[1,0],[-1,0],[0,1],[0,-1],[0,0]])
    cycle = cur_time % modulo
    next_checks = []
    for direction in directions:
        check = tuple([cur_loc[0]+direction[0],cur_loc[1]+direction[1]])
        if check[0] < 0 or check[1] < 0 or check[0] >= len(mymap) or check[1] >= len(mymap[0]):
            continue
        if cycle in mymap[check[0]][check[1]]:
            next_checks.append((check[0],check[1]))
    return next_checks

if __name__ == "__main__":
    with open("day24.txt") as f:
        lines = f.read().split('\n')
    maplen = len(lines) - 2
    maplen2 = len(lines[0]) - 2
    modulo = np.lcm(maplen,maplen2)
    mymap = []
    for i,line in enumerate(lines):
        mymap.append([])
        for j, char in enumerate(line):
            if char == "#":
                mymap[i].append(set([]))
            else:
                mymap[i].append(set([x for x in range(modulo)]))
    for i,line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                continue
            if char == ".":
                continue
            if char == "v":
                cycle = 0
                while cycle < modulo:
                    checkloc = 1 + (i + cycle - 1) % maplen
                    if cycle in mymap[checkloc][j]:
                        mymap[checkloc][j].remove(cycle)
                    cycle += 1
            if char == "^":
                cycle = 0
                while cycle < modulo:
                    checkloc = 1 + (i - cycle - 1) % maplen
                    if cycle in mymap[checkloc][j]:
                        mymap[checkloc][j].remove(cycle)
                    cycle += 1
            if char == ">":
                cycle = 0
                while cycle < modulo:
                    checkloc = 1 + (j + cycle - 1) % maplen2
                    if cycle in mymap[i][checkloc]:
                        mymap[i][checkloc].remove(cycle)
                    cycle += 1
            if char == "<":
                cycle = 0
                while cycle < modulo:
                    checkloc = 1 + (j - cycle - 1) % maplen2
                    if cycle in mymap[i][checkloc]:
                        mymap[i][checkloc].remove(cycle)
                    cycle += 1
    to_check = set([(0,1)])
    cur_time = 0
    while True:
        cur_time += 1
        next_check = set([])
        if (maplen+1,maplen2) in to_check:
            break
        for check in to_check:
            next_checks = get_next_checks(mymap,check,cur_time,modulo)
            for n_check in next_checks:
                next_check.add(tuple(n_check))
        to_check = copy.deepcopy(next_check)
    sol1 = cur_time-1
    to_check = set([(maplen+1,maplen2)])
    cur_time = sol1
    while True:
        cur_time += 1
        next_check = set([])
        if (0,1) in to_check:
            break
        for check in to_check:
            next_checks = get_next_checks(mymap,check,cur_time,modulo)
            for n_check in next_checks:
                next_check.add(tuple(n_check))
        to_check = copy.deepcopy(next_check)
    cur_time -= 1
    to_check = set([(0,1)])
    while True:
        cur_time += 1
        next_check = set([])
        if (maplen+1,maplen2) in to_check:
            break
        for check in to_check:
            next_checks = get_next_checks(mymap,check,cur_time,modulo)
            for n_check in next_checks:
                next_check.add(tuple(n_check))
        to_check = copy.deepcopy(next_check)
    sol2 = cur_time-1

    
    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
