#!/usr/bin/python3

a = str(input())
m = len(a)%2

ans="YES"
for i in range(ord('a'), ord('z')+1):
    c = a.count(chr(i))
    if ((c%2)==1):
        if (m==1):
            m-=1
        else:
            ans="NO"
            break
print(ans)