import numpy as np
import copy

if __name__ == "__main__":
    with open("day6.txt") as f:
        data = f.read()
    sol1 = sol2 = 0
    for i in range(len(data)):
        if not sol1 and len(set(data[i:i+4])) == 4: # only want to check if we haven't found the solution yet
            sol1 = i+4
        if sol1 and len(set(data[i:i+14])) == 14: #only check if we have found solution 1
            sol2 = i+14
            break

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
