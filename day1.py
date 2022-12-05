import numpy as np

if __name__ == "__main__":
    with open("day1.txt") as f:
        (sol1, sol2) = [(totalcal[0], np.sum(totalcal[:3])) for totalcal in [sorted([np.sum([int(cal) for cal in elf.split('\n')]) for elf in f.read().split('\n\n')],reverse=True)]][0]
    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
