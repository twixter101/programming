t = int(input())
b = [0] * t
for i in range(t):
    b[i] = int(input())
    
f = []
f1, f2 = 0, 1
i = 0;
while(1):
    if (f1 > max(b)):
        break
    else:
        f.append(f1)
    f1, f2 = f2, f1+f2
    i += 1

for i in range(t):
    if (b[i] in f):
        print("IsFibo")
    else:
        print("IsNotFibo")