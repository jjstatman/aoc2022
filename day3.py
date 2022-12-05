import numpy as np

if __name__ == "__main__":
    
    with open("day3.txt") as f:
        data = [x for x in f.read().split('\n') if x]
    sol1 = sol2 = 0
    for i, line in enumerate(data):
        val = set(line[:len(line)//2]).intersection(set(line[len(line)//2:])).pop()
        sol1 += (ord(val) - ord('A') + 27) if val.isupper() else (ord(val) - ord('a') + 1)
        if not (i%3):
            val = set(line).intersection(set(data[i+1]),set(data[i+2])).pop()
            sol2 += (ord(val) - ord('A') + 27) if val.isupper() else (ord(val) - ord('a') + 1)

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
