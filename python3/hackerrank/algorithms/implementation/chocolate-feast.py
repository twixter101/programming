for t in range(int(input())):
    n = str(input()).split()
    c1 = int(n[0])//int(n[1])
    c2 = c1//int(n[2])
    t1 = ((c1%int(n[2]))+c2)//int(n[2])
    c3 = t1
    while (t1 >= int(n[2])):
        t1 = ((t1%int(n[2]))+t1)//int(n[2])
        c3 += t1
    print(c1+c2+c3)