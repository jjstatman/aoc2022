import numpy as np
import copy

if __name__ == "__main__":
    sol1 = ""
    sol2 = ""
    
    with open("day5.txt") as f:
        coldat, moves = f.read().split('\n\n')
    moves = [[int(move.split(' ')[1]), int(move.split(' ')[3]), int(move.split(' ')[5])] for move in moves.split('\n')]
    coldat = [[col[1],col[5],col[9],col[13],col[17],col[21],col[25],col[29],col[33]] for col in coldat.split('\n')[:-1]]
    cols = [[] for col in coldat[0]]
    for col in coldat:
        for i, box in enumerate(col):
            if not box == ' ':
                cols[i].append(box)
    cols2 = copy.deepcopy(cols)
    for move in moves:
        for i in range(move[0]):
            cols[move[2]-1].insert(0,cols[move[1]-1].pop(0))
            cols2[move[2]-1].insert(0,cols2[move[1]-1].pop(move[0]-i-1))
    for col in cols:
        sol1 += col[0]
    for col in cols2:
        sol2 += col[0]
    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
