# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 18

import pandas
file = pandas.read_csv('Problem18.csv', header=None)
print(file)
data = []
file.values.tolist()
for n in file.values:
    print(n)
    print(str(n))
    n=str(n[0]).split(' ')
    print(n)
    n = [int(a) for a in n]
    data.append(n)
print(data)
a = len(data)
for i in range(a-1):
    print(data[a-i-2])
    b = len(data[a-i-2])
    for j in range(b):
        print(data[a-i-1][j:j+2])
        data[a-i-2][j]+=max(data[a-i-1][j:j+2])
    print(data[a-i-2])
    data.pop()