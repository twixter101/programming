#!/usr/bin/python3

l = int(input())
r = int(input())
if (l == r):
    print(0)
else:
    m = [0] * ((r-l)**2)
    k = 0
    for i in range(l, r):
        for j in range(l+1, r+1):
            if (i != j):
                m[k] = i^j
                #print(i, j, m[k])
                k += 1
    print(max(m))