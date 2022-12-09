import numpy as np
import copy

if __name__ == "__main__":
    with open("day9.txt") as f:
        data = [x for x in f.read().split("\n") if x]
    data2 = []
    for x in data:
        y = x.split(' ')
        data2.append((y[0], int(y[1])))
    direc = {'R':np.array([1,0]),'L':np.array([-1,0]),'U':np.array([0,1]),'D':np.array([0,-1])}
    rope = np.zeros([10,2])
    lastrope = rope
    visited = {}
    visited[tuple(rope[1])] = True
    visited2 = {}
    visited2[tuple(rope[9])] = True
    for command in data2:
        for i in range(command[1]):
            rope[0] = rope[0] + direc[command[0]]
            for j in range(1,10):
                if max(abs(rope[j-1]-rope[j])) > 1:
                    diff = rope[j-1] - rope[j] # make it so max(abs(diff)) < 2
                    if diff[0] > 1:
                        diff[0] -= 1
                    if diff[0] < -1:
                        diff[0] += 1
                    if diff[1] > 1:
                        diff[1] -= 1
                    if diff[1] < -1:
                        diff[1] += 1
                    rope[j] += diff
                    if j == 1:
                        visited[tuple(rope[1])] = True
                    if j == 9:
                        visited2[tuple(rope[9])] = True
            lastrope = copy.deepcopy(rope)

    sol1 = len(visited)
    sol2 = len(visited2)

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
