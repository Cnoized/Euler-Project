# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 42

import pandas
file = pandas.read_csv('Problem42.csv', header=None, dtype = str)
print(file)
data = []
file.values.tolist()
for n in file.values:
    print(n)
    print(str(n))
    # n=str(n[0]).split(' ')
    print(n)
    for a in n:
        data.append(a)
print(data)
print(ord('A')-64)
L=[]
for a in data:
    name = sum([ord(i)-64 for i in a])
    i=1
    while name>0:
        name -= i
        i+=1
        if name == 0:
            L.append(a)
print(len(L))