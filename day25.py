import numpy as np
import copy
import json
from functools import cmp_to_key

def to_base_5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n //=5
    return s

add_char = {"=":"-","-":"0","0":"1","1":"2","2":"3"}

if __name__ == "__main__":
    with open("day25-2.txt") as f:
        nums = f.read().split('\n')

    mysum = 0
    for num in nums:
        mynum = 0
        for j,char in enumerate(num[::-1]):
            if char == "2":
                mynum += 2*(5**j)
            elif char == "1":
                mynum += 1*(5**j)
            elif char == "0":
                mynum += 0*(5**j)
            elif char == "-":
                mynum += -1*(5**j)
            elif char == "=":
                mynum += -2*(5**j)
        mysum += mynum
    mynum = to_base_5(mysum)
    mynum = [char for char in mynum]
    while True:
        if "3" in mynum or "4" in mynum:
            need_add = False
            for j,char in enumerate(mynum):
                if char == "3":
                    if j == 0:
                        need_add = True
                    else:
                        mynum[j-1] = add_char[mynum[j-1]]
                    mynum[j] = "="
                if char == "4":
                    if j == 0:
                        need_add = True
                    else:
                        mynum[j-1] = add_char[mynum[j-1]]
                    mynum[j] = "-"
            if need_add:
                mynum = "1" + mynum
        else:
            break
    sol1 = ""
    for char in mynum:
        sol1 += char
    
    print('Solution 1:', sol1)
