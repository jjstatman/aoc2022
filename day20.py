import numpy as np
import copy
import json
from functools import cmp_to_key

def mix(data, num_mixes=1):
    datalen = len(data)
    newdata = copy.deepcopy(data)
    for _ in range(num_mixes):
        for val in data:
            if val[1] == 0:
                zeroentry = val
            index = newdata.index(val)
            newval = newdata.pop(index)
            newindex = (index+val[1]) % (datalen-1)
            if newindex:
                newdata.insert(newindex, newval)
            else:
                newdata.append(newval)

    zeroindex = newdata.index(zeroentry)

    indeces = (np.array([1000,2000,3000]) + zeroindex) % datalen
    outval = 0
    for index in indeces:
        outval += newdata[index][1]
    return outval


if __name__ == "__main__":
    with open("day20.txt") as f:
        data = [(ind, int(val)) for ind, val in enumerate(f.read().split('\n'))]
    data2 = []
    for val in data:
        data2.append((val[0],val[1]*811589153))
    sol1 = mix(data)
    sol2 = mix(data2,10)

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
