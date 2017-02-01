N, M = str(input()).split()
jars = 0
for i in range(int(M)):
    l = list(str(input()).split())
    jars += ((int(l[1])-int(l[0]))+1)*int(l[2])
print(jars//int(N))