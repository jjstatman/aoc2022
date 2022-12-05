import numpy as np

if __name__ == "__main__":
    score = {}
    score[('A','X')] = [1 + 3, 3 + 0]
    score[('A','Y')] = [2 + 6, 1 + 3]
    score[('A','Z')] = [3 + 0, 2 + 6]
    score[('B','X')] = [1 + 0, 1 + 0]
    score[('B','Y')] = [2 + 3, 2 + 3]
    score[('B','Z')] = [3 + 6, 3 + 6]
    score[('C','X')] = [1 + 6, 2 + 0]
    score[('C','Y')] = [2 + 0, 3 + 3]
    score[('C','Z')] = [3 + 3, 1 + 6]
    with open("day2.txt") as f:
        sol1, sol2 = np.sum(np.array([score[tuple(x.split(' '))] for x in f.read().split('\n')]),axis=0)
    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
