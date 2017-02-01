#!/usr/bin/python3

inputdata = str(input())
testcase = inputdata.split()

inputdata = str(input())
segment = inputdata.split()

for i in range(int(testcase[1])):
    inputdata = str(input())
    service = inputdata.split()

    print(min(segment[int(service[0]):int(service[1])+1]))
    