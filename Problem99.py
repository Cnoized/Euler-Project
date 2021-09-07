# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 99

from math import log

import pandas
file = pandas.read_csv('Problem99.txt', header=None)
print(file)
data = []
file.values.tolist()
data = [list(a) for a in file.values]
print(data)

Largest = 0

for line in range(len(data)):
    Value = log(data[line][0])*data[line][1]
    if Value > Largest:
        Largest = Value
        MaxLine = line
        print(MaxLine+1)