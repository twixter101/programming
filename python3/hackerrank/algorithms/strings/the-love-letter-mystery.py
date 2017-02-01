#!/usr/bin/python3

lovelettercount = int(input())
for h in range(lovelettercount):
    loveletter = list(str(input()))

    fullcount=len(loveletter)-1
    halfcount=(fullcount+1)//2

    opcount=0
    for i in range(halfcount):
        if (loveletter[i] < loveletter[fullcount-i]):
            while (loveletter[i] < loveletter[fullcount-i]):
                loveletter[fullcount-i] = chr(ord(loveletter[fullcount-i])-1)
                opcount += 1
        elif (loveletter[i] > loveletter[fullcount-i]):
            while (loveletter[i] > loveletter[fullcount-i]):
                loveletter[i] = chr(ord(loveletter[i])-1)
                opcount += 1
            
    print(opcount)