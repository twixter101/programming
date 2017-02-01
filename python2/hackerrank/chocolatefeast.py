#!/usr/bin/python3

for t in range(int(input())):
    n, c, m = list(int(x) for x in input().split())
    c1 = n//c
    c2 = c1//m
    t1 = ((c1%m)+c2)//m
    c3 = t1
    while (t1 >= m):
        t1 = ((t1%m)+t1)//m
        c3 += t1
    print(c1+c2+c3)
    #n = str(input()).split()
    #c1 = int(n[0])//int(n[1])
    #c2 = c1//int(n[2])
    #t1 = ((c1%int(n[2]))+c2)//int(n[2])
    #c3 = t1
    #while (t1 >= int(n[2])):
    #    t1 = ((t1%int(n[2]))+t1)//int(n[2])
    #    c3 += t1
    #print(c1+c2+c3)
