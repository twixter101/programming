#!/usr/bin/python3

lovelettercount = int(input())
for h in range(lovelettercount):
    loveletter = list(str(input()))

    opcount=0
    fullcount=len(loveletter)-1
    halfcount=(fullcount+1)//2

    for i in range(halfcount):
        #print(loveletter[i], loveletter[fullcount-i])
        if (loveletter[i] < loveletter[fullcount-i]):
            while (loveletter[i] < loveletter[fullcount-i]):
                loveletter[fullcount-i] = chr(ord(loveletter[fullcount-i])-1)
                #print(loveletter[i], loveletter[fullcount-i])
                opcount += 1
        elif (loveletter[i] > loveletter[fullcount-i]):
            while (loveletter[i] > loveletter[fullcount-i]):
                loveletter[i] = chr(ord(loveletter[i])-1)
                #print(loveletter[i], loveletter[fullcount-i])
                opcount += 1
            
    #print("".join(loveletter), opcount)
    print(opcount)

        
    
    