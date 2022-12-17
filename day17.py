import numpy as np
import copy
import json
from functools import cmp_to_key

def check_lr_collision(rock_map,location,rock,jet):
    for y, line in enumerate(rock):
        for x, val in enumerate(line):
            if not val:
                continue
            if location[0] + jet + x < 0 or location[0] + jet + x >= 7 or (location[0] + x + jet, location[1] + y) in rock_map:
                return 0
    return 1

def check_ud_collision(rock_map,location,rock):
    for y, line in enumerate(rock):
        for x, val in enumerate(line):
            if not val:
                continue
            if location[1] + y - 1 < 0 or (location[0] + x,location[1] + y - 1) in rock_map:
                return 0
    return 1



if __name__ == "__main__":
    with open("day17.txt") as f:
        data = [-1 if x == '<' else 1 for x in f.read()]
    rocks = [[[1,1,1,1]],[[0,1,0],[1,1,1],[0,1,0]],[[1,1,1],[0,0,1],[0,0,1]],[[1],[1],[1],[1]],[[1,1],[1,1]]]
    max_h = -1
    start_x = 2
    rock_map = {}
    k = 0
    last_i = 0
    last_h = 0
    last_di = 0
    last_dh = 0
    delta_h = 0
    delta_i = 0
    sol2 = 0
    to_go = 1000000000000
    for i in range(1000000000000):
        rock = rocks[i % 5]
        location = [start_x,max_h+4]
        if i == 2022:
            sol1 = max_h+1
        if i > to_go:
            sol2 += max_h
            break
        while True:
            jet = data[k]
            k += 1
            if k >= len(data):
                k = 0
                last_dh = delta_h
                last_di = delta_i
                delta_h = max_h-last_h
                delta_i = i-last_i
                last_i = i
                last_h = max_h
                if delta_h == last_dh and delta_i == last_di and delta_h and delta_i and not sol2:
                    period = delta_i
                    increase = delta_h
                    num_cycles = (1000000000000-i)//delta_i
                    to_go = ((1000000000000-i)/delta_i - num_cycles)*delta_i + i
                    sol2 = num_cycles*increase
            if check_lr_collision(rock_map,location,rock,jet):
                location[0] += jet
            if check_ud_collision(rock_map,location,rock):
                location[1] -= 1
            else:
                for y, line in enumerate(rock):
                    for x, val in enumerate(line):
                        if val:
                            rock_map[(location[0]+x,location[1]+y)] = 1
                            if location[1] + y > max_h:
                                max_h = location[1] + y
                break

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
