testcase = int(input())
for t in range(testcase):
    n = int(input())
    a = int(input())
    b = int(input())
    
    r = [0] * n
    for i in range(n):
        r[i] = (((n-1)-i)*a)+(i*b)
    
    s = list(set(r))
    s.sort()
    print(' '.join(str(x) for x in s))