#!/usr/bin/python3

import re

c = int(input())
g = [0] * 26
for i in range(c):
    s = str(input())
    t = [0] * 26

    for j in range(len(s)):
        if (t[ord(s[j])-ord('a')] == 0):
            g[ord(s[j])-ord('a')] += 1
            t[ord(s[j])-ord('a')] += 1

print(g.count(c))