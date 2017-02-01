#!/usr/bin/python3

N, M = str(input()).split()
#jars = [0] * int(N)
jars = 0
for i in range(int(M)):
    l = list(str(input()).split())
    #for j in range(int(l[0])-1, int(l[1])):
    #    jars[j] += int(l[2])
    #print(jars)
    jars += ((int(l[1])-int(l[0]))+1)*int(l[2])
print(jars//int(N))