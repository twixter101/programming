#!/bin/python
def nextMove(n,r,c,grid):
    if r > pPos[0]:
        return "UP"
    elif r < pPos[0]:
        return "DOWN"
    elif c > pPos[1]:
        return "LEFT"
    elif c < pPos[1]:
        return "RIGHT"
    else:
        return


n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
pPos = []
for i in xrange(0, n):
    lGrid = list(raw_input())
    grid.append(lGrid)

    if 'p' in lGrid:
        pPos = [i, lGrid.index("p")]

print nextMove(n,r,c,grid)
