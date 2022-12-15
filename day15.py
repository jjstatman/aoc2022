import numpy as np
import copy
import json
from functools import cmp_to_key

if __name__ == "__main__":
    with open("day15.txt") as f:
        data = [x for x in f.read().split('\n')]
    sensors = {}
    for line in data:
        sensor = [int(x.split('=')[1]) for x in line.split(':')[0].split(', ')]
        beacon = [int(x.split('=')[1]) for x in line.split(':')[1].split(', ')]
        sensors[tuple(sensor)] = (tuple(beacon),abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1]))
    row = 2000000
    #use super bad method to calculate because i don't want to hard code any bounds
    #and i'm too lazy to figure out intersecting intervals
    invalid = {}
    for sensor in sensors:
        beacon = sensors[sensor][0]
        dist = sensors[sensor][1]
        if abs(sensor[1]-row) <= dist:
            xdist = dist - abs(sensor[1]-row)
            for i in range(-xdist, xdist+1):
                invalid[i+sensor[0]] = 1
    for sensor in sensors:
        if sensors[sensor][0][1] == row:
            invalid[sensors[sensor][0][0]] = 0
    sol1 = sum(invalid.values())
    sol2 = 0
    #super bad method is way too slow, take intervals, do inefficient way to figure out intersections
    for i in range(4000001):
        if not i % 100000:
            print(i)
        invalid = []
        for sensor in sensors:
            dist = sensors[sensor][1]
            if abs(sensor[1]-i) <= dist:
                xdist = dist - abs(sensor[1]-i)
                vals = [max(0,sensor[0]-xdist),min(sensor[0]+xdist,4000000)]
                invalid.append(vals)
        j = 0
        while j <= 4000000:
            for dist in invalid:
                if j >= dist[0] and j <= dist[1]:
                    j = dist[1]+1
                    break
            else:
                sol2 = 4000000*j + i
                break
        if sol2:
            break


    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
