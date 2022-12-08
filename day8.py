import numpy as np
import copy

if __name__ == "__main__":
    with open("day8.txt") as f:
        data = np.array([[int(y) for y in x] for x in f.read().split("\n") if x])
    sol1 = sol2 = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if i == 0 or j == 0 or i == len(data)-1 or j == len(data[0])-1:
                sol1 += 1
                continue
            tree = data[i,j]
            if tree > max(data[:i,j]) or tree > max(data[i+1:,j]) or tree > max(data[i,:j]) or tree > max(data[i,j+1:]):
                sol1 += 1


    for i in range(len(data)):
        for j in range(len(data[0])):
            if i == 0 or j == 0 or i == len(data)-1 or j == len(data[0])-1: # score is 0
                continue
            val = 1
            tree = data[i,j]

            x = i-1
            while x > 0: #search left
                if data[x,j] >= tree:
                    break
                x -= 1
            val *= i-x

            x = i+1 #search right
            while x < len(data)-1:
                if data[x,j] >= tree:
                    break
                x += 1
            val *= x-i

            y = j-1
            while y > 0: #search up
                if data[i,y] >= tree:
                    break
                y -= 1
            val *= j-y

            y = j+1
            while y < len(data[0])-1: #search down
                if data[i,y] >= tree:
                    break
                y += 1
            val *= y-j

            if val > sol2:
                sol2 = val

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
