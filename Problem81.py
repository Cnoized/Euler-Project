# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 81
import numpy

import pandas
file = pandas.read_csv('Problem81.txt', header=None)
print(file)
data = []
file.values.tolist()

for n in file.values:
    Values = [a for a in n]+[10000000]
    data.append(Values)

    # print(n)
    # print(data)
    # print(type(data))
data.append([10000000]*81)

    
for n in range(1,80):
    minimum = 0
    for a in range(n+1):
        # print(79-n+a,79-a)
        # print(data[79-n+a][79-a])
        # print(data[79-n+a+1][79-a])
        # print(data[79-n+a][79-a+1])
        # input()
        data[79-n+a][79-a]+=min(data[79-n+a+1][79-a],data[79-n+a][79-a+1])
        if minimum == 0:
            minimum = data[79-n+a][79-a]
        else:
            if data[79-n+a][79-a]<minimum:
                minimum = data[79-n+a][79-a]
for n in range(80):
    minimum = 0
    for a in range(79-n):
            
        
        # print(78-n-a,a)
        # print(data[78-n-a][a])
        # print(data[78-n-a+1][a])
        # print(data[78-n-a][a+1])
        # input()
        data[78-n-a][a]+=min(data[78-n-a+1][a],data[78-n-a][a+1])
        if minimum == 0:
            minimum = data[78-n-a][a]
        else:
            if data[78-n-a][a]<minimum:
                minimum = data[78-n-a][a]
    print(minimum)
print(data[0][0])