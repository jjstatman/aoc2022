import numpy as np
import copy
import json
from functools import cmp_to_key

class Room:
    def __init__(self,raw):
        self.name = raw.split(' has ')[0].split(' ')[1]
        self.rate = int(raw.split('=')[1].split(';')[0])
        if len(raw.split('valves ')) > 1:
            self.tunnel = raw.split('valves ')[1].split(', ')
        else:
            self.tunnel = [raw.split('valve ')[-1]]

def findminpath(rooms,srcroom,destroom):
    pathlen = 0
    if srcroom == destroom:
        return pathlen
    tocheck = [srcroom]
    checked = set([])
    while True:
        nextcheck = set([])
        for room in tocheck:
            if destroom in rooms[room].tunnel:
                return pathlen+1
            else:
                for nextroom in rooms[room].tunnel:
                    if not nextroom in checked:
                        nextcheck.add(nextroom)
                checked.add(room)
        pathlen += 1
        tocheck = copy.deepcopy(nextcheck)

def find_best_score(cur_room,rooms,dists,visited,time_left):
    best_score = 0
    for path in dists:
        if not path[0] == cur_room:
            continue
        next_room = path[1]
        cost = dists[path]
        if cost >= time_left:
            continue
        if next_room in visited:
            continue
        new_visited = copy.deepcopy(visited)
        new_visited.append(cur_room)
        branch_score = find_best_score(next_room,rooms,dists,new_visited,time_left-cost) + rooms[next_room].rate*(time_left-cost)
        if branch_score > best_score:
            best_score = branch_score
    return best_score

def find_best_score2(cur_room,trav_time,cur_room2,trav_time2,rooms,dists,visited,time_left):
    best_score = 0
    if not trav_time and trav_time2:
        for path in dists:
            if not path[0] == cur_room:
                continue
            next_room = path[1]
            cost = dists[path]
            if cost >= time_left:
                continue
            if cost > trav_time2:
                continue
            if next_room in visited:
                continue
            new_visited = copy.deepcopy(visited)
            new_visited.append(next_room)
            branch_score = find_best_score2(next_room,trav_time,cur_room2,trav_time2-cost,rooms,dists,new_visited,time_left-cost) + rooms[next_room].rate*(time_left-cost)
            if branch_score > best_score:
                best_score = branch_score

        for path in dists:
            if not path[0] == cur_room:
                continue
            next_room = path[1]
            cost = dists[path]
            if cost >= time_left:
                continue
            if next_room in visited:
                continue
            if cost <= trav_time2:
                continue
            for path2 in dists:
                if not path2[0] == cur_room2 or path[1] == path2[1]:
                    continue
                next_room2 = path2[1]
                cost2 = dists[path2]
                if cost2 >= time_left - trav_time2:
                    continue
                if next_room2 in visited:
                    continue
                new_visited = copy.deepcopy(visited)
                new_visited.append(next_room)
                new_visited.append(next_room2)
                if cost2 + trav_time2 > cost:
                    new_trav_time2 = cost2 + trav_time2 - cost
                    new_trav_time = 0
                elif cost > cost2 + trav_time2:
                    new_trav_time = cost - cost2 - trav_time2
                    new_trav_time2 = 0
                else:
                    new_trav_time = 0
                    new_trav_time2 = 0
                branch_score = find_best_score2(next_room,new_trav_time,next_room2,new_trav_time2,rooms,dists,new_visited,time_left-min(cost,cost2+trav_time2)) + rooms[next_room].rate*(time_left-cost) + rooms[next_room2].rate*(time_left-cost2-trav_time2)
                if branch_score > best_score:
                    best_score = branch_score
 

    elif trav_time and not trav_time2:
        for path2 in dists:
            if not path2[0] == cur_room2:
                continue
            next_room2 = path2[1]
            cost2 = dists[path2]
            if cost2 >= time_left:
                continue
            if cost2 > trav_time:
                continue
            if next_room2 in visited:
                continue
            new_visited = copy.deepcopy(visited)
            new_visited.append(next_room2)
            branch_score = find_best_score2(cur_room,trav_time-cost2,next_room2,trav_time2,rooms,dists,new_visited,time_left-cost2) + rooms[next_room2].rate*(time_left-cost2)
            if branch_score > best_score:
                best_score = branch_score

        for path2 in dists:
            if not path2[0] == cur_room2:
                continue
            next_room2 = path2[1]
            cost2 = dists[path2]
            if cost2 >= time_left:
                continue
            if next_room2 in visited:
                continue
            if cost2 <= trav_time:
                continue
            for path in dists:
                if not path[0] == cur_room or path[1] == path2[1]:
                    continue
                next_room = path[1]
                cost = dists[path]
                if cost >= time_left - trav_time:
                    continue
                if next_room in visited:
                    continue
                new_visited = copy.deepcopy(visited)
                new_visited.append(next_room)
                new_visited.append(next_room2)
                if cost + trav_time > cost2:
                    new_trav_time = cost + trav_time - cost2
                    new_trav_time2 = 0
                elif cost2 > cost + trav_time:
                    new_trav_time2 = cost2 - cost - trav_time
                    new_trav_time = 0
                else:
                    new_trav_time = 0
                    new_trav_time2 = 0
                branch_score = find_best_score2(next_room,new_trav_time,next_room2,new_trav_time2,rooms,dists,new_visited,time_left-min(cost2,cost+trav_time)) + rooms[next_room2].rate*(time_left-cost2) + rooms[next_room].rate*(time_left-cost-trav_time)
                if branch_score > best_score:
                    best_score = branch_score
 
    else:
        if time_left == 26:
            #don't search (b,a) if we've already searched (a,b)
            searched = []
        for path in dists:
            if not path[0] == cur_room:
                continue
            if time_left == 26:
                searched.append(path[1])
            next_room = path[1]
            cost = dists[path]
            if cost >= time_left:
                continue
            if next_room in visited:
                continue
            for path2 in dists:
                if time_left == 26:
                    if path2[1] in searched:
                        continue
                if not path2[0] == cur_room2 or path[1] == path2[1]:
                    continue
                next_room2 = path2[1]
                cost2 = dists[path2]
                if cost2 >= time_left:
                    continue
                if next_room2 in visited:
                    continue
                new_visited = copy.deepcopy(visited)
                new_visited.append(next_room)
                new_visited.append(next_room2)
                if cost2 > cost:
                    new_trav_time2 = cost2 - cost
                    new_trav_time = 0
                elif cost > cost2:
                    new_trav_time = cost - cost2
                    new_trav_time2 = 0
                else:
                    new_trav_time = 0
                    new_trav_time2 = 0
                branch_score = find_best_score2(next_room,new_trav_time,next_room2,new_trav_time2,rooms,dists,new_visited,time_left-min(cost,cost2)) + rooms[next_room].rate*(time_left-cost) + rooms[next_room2].rate*(time_left-cost2)
                if branch_score > best_score:
                    best_score = branch_score
                #debug tracker
                if time_left == 26:
                    print(next_room,new_trav_time,next_room2,new_trav_time2,cost,cost2,branch_score,time_left,best_score)
    #see if it is better to finish with one person
    test_score = find_best_score(cur_room,rooms,dists,visited,time_left-trav_time)
    if test_score > best_score:
        best_score = test_score
    test_score = find_best_score(cur_room2,rooms,dists,visited,time_left-trav_time2)
    if test_score > best_score:
        best_score = test_score

    return best_score



if __name__ == "__main__":
    with open("day16.txt") as f:
        data = [x for x in f.read().split('\n')]
    rooms = {}
    for line in data:
        newroom = Room(line)
        rooms[newroom.name] = newroom

    dists = {}
    start = "AA"

    for room in rooms:
        if not rooms[room].rate and not room == start:
            continue
        for room2 in rooms:
            if room == room2:
                continue
            if not rooms[room2].rate:
                continue
            cost = findminpath(rooms,room,room2)
            dists[(room,room2)] = cost+1 #plus one because we always go to turn on

    sol1 = find_best_score(start,rooms,dists,[],30)
    sol2 = find_best_score2(start,0,start,0,rooms,dists,[],26)

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
