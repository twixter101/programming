#!/bin/python

def displayPathtoPrincess(n,grid):
    #print all the moves here
    if mPos[0] > pPos[0]:
        grid[mPos[0]][mPos[1]] = '-'
        mPos[0] -= 1
        grid[mPos[0]][mPos[1]] = 'm'
        print "UP"
    elif mPos[0] < pPos[0]:
        grid[mPos[0]][mPos[1]] = '-'
        mPos[0] += 1
        grid[mPos[0]][mPos[1]] = 'm'
        print "DOWN"
    elif mPos[1] > pPos[1]:
        grid[mPos[0]][mPos[1]] = '-'
        mPos[1] -= 1
        grid[mPos[0]][mPos[1]] = 'm'
        print "LEFT"
    elif mPos[1] < pPos[1]:
        grid[mPos[0]][mPos[1]] = '-'
        mPos[1] += 1
        grid[mPos[0]][mPos[1]] = 'm'
        print "RIGHT"
    else:
        return
        
    return displayPathtoPrincess(n,grid)

m = input()

grid = []
mPos = []
pPos = []
for i in xrange(0, m):
    lGrid = list(raw_input().strip())
    grid.append(lGrid)

    if 'm' in lGrid:
        mPos = [i, lGrid.index("m")]

    if 'p' in lGrid:
        pPos = [i, lGrid.index("p")]

displayPathtoPrincess(m,grid)
