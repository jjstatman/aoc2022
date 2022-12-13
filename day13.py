import numpy as np
import copy
import json
from functools import cmp_to_key

def compare_pair(left,right):
    for i in range(min(len(left),len(right))):
        if isinstance(left[i], list):
            if isinstance(right[i], list):
                val = compare_pair(left[i],right[i])
                if val == 0:
                    continue
                else:
                    return val
            else:
                val = compare_pair(left[i],[right[i]])
                if val == 0:
                    continue
                else:
                    return val
        else:
            if isinstance(right[i], list):
                val = compare_pair([left[i]],right[i])
                if val == 0:
                    continue
                else:
                    return val
            else:
                if left[i] < right[i]:
                    return -1
                elif left[i] > right[i]:
                    return 1
                else:
                    continue
    else:
        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
            return 1
        else:
            return 0

if __name__ == "__main__":
    with open("day13.txt") as f:
        data = [[json.loads(y) for y in x.split('\n')] for x in f.read().split("\n\n") if x]

    sol1 = 0
    data2 = []
    for i, pair in enumerate(data):
        data2.append(pair[0])
        data2.append(pair[1])
        if compare_pair(pair[0],pair[1]) < 0:
            sol1 += i+1

    data2.append([[2]])
    data2.append([[6]])

    data2.sort(key=cmp_to_key(compare_pair))

    sol2 = 0
    for i in range(len(data2)):
        if data2[i] == [[2]]:
            sol2 = (i+1)
        elif data2[i] == [[6]]:
            sol2 *= (i+1)

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
