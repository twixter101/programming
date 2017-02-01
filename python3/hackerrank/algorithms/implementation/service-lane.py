#!/usr/bin/python3

inputdata = str(input())
testcase = inputdata.split()

inputdata = str(input())
segment = inputdata.split()

for i in range(int(testcase[1])):
    inputdata = str(input())
    service = inputdata.split()

    vehicle = 3
    for j in range(int(service[0]), int(service[1]) + 1):
        if (segment[j] == '1'):
            vehicle = 1
            break
        elif (segment[j] == '2'):
            vehicle = 2
    print(vehicle)