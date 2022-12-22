import numpy as np
import copy
import json
from functools import cmp_to_key

def move_forward(mymap,loc,direc):
    dimensions = mymap.shape
    newloc = np.array(copy.deepcopy(loc))
    newloc = newloc + direc
    newloc[0] = newloc[0] % mymap.shape[0]
    newloc[1] = newloc[1] % mymap.shape[1]
    if mymap[tuple(newloc)] == 1:
        return newloc
    if mymap[tuple(newloc)] == 0:
        while mymap[tuple(newloc)] == 0:
            newloc = newloc+direc
            newloc[0] = newloc[0] % mymap.shape[0]
            newloc[1] = newloc[1] % mymap.shape[1]
        if mymap[tuple(newloc)] == -1:
            return loc
        else:
            return newloc
    if mymap[tuple(newloc)] == -1:
        return loc

def get_face(loc,faces):
    return faces[loc[0]//50][loc[1]//50]

def move_forward2(mymap,loc,direc,dirs,faces):
    curdir = dirs[direc]
    dimensions = mymap.shape
    newloc = np.array(copy.deepcopy(loc))
    newloc = newloc + curdir
    newloc[0] = newloc[0] % mymap.shape[0]
    newloc[1] = newloc[1] % mymap.shape[1]
    if mymap[tuple(newloc)] == 1:
        return newloc, direc
    if mymap[tuple(newloc)] == 0:
        oldface = faces[loc[0]//50][loc[1]//50]
        if oldface == 1:
            if direc == 2:
                newloc = np.array([149-loc[0],0])
                newdir = 0
            elif direc == 3:
                newloc = np.array([100+loc[1],0])
                newdir = 0
        elif oldface == 2:
            if direc == 0:
                newloc = np.array([149-loc[0],99])
                newdir = 2
            elif direc == 1:
                newloc = np.array([loc[1]-50,99])
                newdir = 2
            elif direc == 3:
                newloc = np.array([199,loc[1]-100])
                newdir = 3
        elif oldface == 3:
            if direc == 0:
                newloc = np.array([49,loc[0]+50])
                newdir = 3
            elif direc == 2:
                newloc = np.array([100,loc[0]-50])
                newdir = 1
        elif oldface == 4:
            if direc == 2:
                newloc = np.array([149-loc[0],50])
                newdir = 0
            elif direc == 3:
                newloc = np.array([loc[1]+50,50])
                newdir = 0
        elif oldface == 5:
            if direc == 0:
                newloc = np.array([149-loc[0],149])
                newdir = 2
            elif direc == 1:
                newloc = np.array([loc[1]+100,49])
                newdir = 2
        elif oldface == 6:
            if direc == 0:
                newloc = np.array([149,loc[0]-100])
                newdir = 3
            elif direc == 1:
                newloc = np.array([0,loc[1]+100])
                newdir = 1
            elif direc == 2:
                newloc = np.array([0,loc[0]-100])
                newdir = 1
        if mymap[tuple(newloc)] == -1:
            return loc, direc
        else:
            return newloc, newdir
    if mymap[tuple(newloc)] == -1:
        return loc, direc

if __name__ == "__main__":
    with open("day22.txt") as f:
        rawmap, instr = f.read().split('\n\n')
    mapsz = (len(rawmap.split('\n')),max([len(x) for x in rawmap.split('\n')]))
    mymap = np.zeros(mapsz)
    for j, line in enumerate(rawmap.split('\n')):
        if not line:
            continue
        for i, char in enumerate(line):
            if char == ".":
                mymap[j,i] = 1
            elif char == "#":
                mymap[j,i] = -1
    face = 1
    faces = []
    for i in range(mymap.shape[0]//50):
        faces.append([])
        for j in range(mymap.shape[1]//50):
            if mymap[50*i,50*j]:
                faces[i].append(face)
                face += 1
            else:
                faces[i].append(0)
    index = 0
    myinstr = []
    dirs = np.array([[0,1],[1,0],[0,-1],[-1,0]])
    curdir = 0
    while index < len(instr):
        if instr[index] == "L" or instr[index] == "R":
            myinstr.append((instr[index],1))
            index += 1
        else:
            lind = instr.find('L',index)
            rind = instr.find('R',index)
            if lind < 0:
                lind = len(instr)
            if rind < 0:
                rind = len(instr)
            myinstr.append(int(instr[index:min(lind,rind)]))
            index = min(lind,rind)
    index = 0
    while index < len(mymap[0]):
        if mymap[0,index] == 1:
            break
        index += 1
    startloc = np.array([0,index])
    curloc = np.array([0,index])
    for instr in myinstr:
        if isinstance(instr,int):
            for _ in range(instr):
                curloc = move_forward(mymap,curloc,dirs[curdir])
        else:
            if instr[0] == "R":
                curdir += instr[1]
                curdir %= 4
            else:
                curdir -= instr[1]
                curdir %=4

    sol1 = 1000*(curloc[0]+1) + (curloc[1]+1)*4 + curdir
    curloc = startloc
    curdir = 0
    for instr in myinstr:
        if isinstance(instr,int):
            for _ in range(instr):
                newloc,newdir = move_forward2(mymap,curloc,curdir,dirs,faces)
                if np.all(curloc == newloc) and curdir == newdir:
                    break
                curloc = newloc
                curdir = newdir

        else:
            if instr[0] == "R":
                curdir += instr[1]
                curdir %= 4
            else:
                curdir -= instr[1]
                curdir %=4

    sol2 = 1000*(curloc[0]+1) + (curloc[1]+1)*4 + curdir

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
