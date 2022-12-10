import numpy as np
import copy

def getval(cycle, vals):
    coords = np.array(sorted(vals.keys()))
    for i, key in enumerate(coords):
        if key >= cycle:
            break
    else:
        return vals[coords[i]]
    if i == 0:
        return 1
    return vals[coords[i-1]]

if __name__ == "__main__":
    with open("day10.txt") as f:
        data = [x for x in f.read().split("\n") if x]
    x = 1
    cycle = 0
    vals = {}
    for line in data:
        cmd = line.split(' ')
        if cmd[0] == 'noop':
            cycle += 1
            continue
        else:
            cycle += 2
            x += int(cmd[1])
            vals[cycle] = x
            continue

    sol1_pts = [20,60,100,140,180,220]
    sol1 = 0

    sol2 = ""
    #i in cycles
    for i in range(1,241):
        coord = getval(i,vals)
        #row is 0-indexed
        row = (i-1)//40
        #check pixel (0-index) with coord value
        if i-2-row*40<= coord and coord <= i-row*40:
            sol2 += "#"
        else:
            sol2 += "."
        #format with newline
        if not i % 40:
            sol2 += '\n'
        #get sol1 answer
        if i in sol1_pts:
            sol1 += i*coord

    print('Solution 1:', sol1)
    print('Solution 2:\n' + sol2)
