#!/usr/bin/python3

for t in range(int(input())):
    n = int(input())
    l = list(str(n))
    c = 0
    for i in range(len(l)):
        try:
            if ((n%int(l[i])) == 0):
                c += 1
        except ZeroDivisionError:
            continue
    print(c)