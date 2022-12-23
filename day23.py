import numpy as np
import copy
import json
from functools import cmp_to_key

if __name__ == "__main__":
    with open("day23.txt") as f:
        lines = f.read().split('\n')

    mymap = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                mymap[(j,len(lines)-i-1)] = 1

    directions = [[0,1],[0,-1],[-1,0],[1,0]] #N,S,W,E
    checks = [[[0,1],[1,1],[-1,1]],[[0,-1],[1,-1],[-1,-1]],[[-1,0],[-1,1],[-1,-1]],[[1,0],[1,1],[1,-1]]]
    adj = [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]
    sol2 = 0
    to_change = True
    while to_change:
        to_change = False
        req = {}
        for elf in mymap:
            for ad in adj:
                if (elf[0]+ad[0],elf[1]+ad[1]) in mymap:
                    break
            else:
                req[elf] = elf
                continue
            for i in range(4):
                for check in checks[i]:
                    if (elf[0]+check[0],elf[1]+check[1]) in mymap:
                        break
                else:
                    req[elf] = (elf[0]+directions[i][0],elf[1]+directions[i][1])
                    break
            else:
                req[elf] = elf
        nextmap = {}
        for elf in mymap:
            elfreq = req.pop(elf)
            if elfreq in req.values():
                nextmap[elf] = 1
            else:
                if not elf == elfreq:
                    to_change = True
                nextmap[elfreq] = 1
            req[elf] = elfreq
        sol2 += 1
        mymap = copy.deepcopy(nextmap)

        nextdir = directions.pop(0)
        directions.append(nextdir)
        nextchecks = checks.pop(0)
        checks.append(nextchecks)
        if sol2 == 10:

            minind = None
            maxind = None
            for elf in mymap:
                if minind == None:
                    minind = list(elf)
                    maxind = list(elf)
                if elf[0] < minind[0]:
                    minind[0] = elf[0]
                if elf[1] < minind[1]:
                    minind[1] = elf[1]
                if elf[0] > maxind[0]:
                    maxind[0] = elf[0]
                if elf[1] > maxind[1]:
                    maxind[1] = elf[1]
            sol1 = (maxind[0]-minind[0]+1)*(maxind[1]-minind[1]+1)-len(mymap)
    
    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
