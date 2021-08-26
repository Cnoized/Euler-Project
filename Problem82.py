# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 82

import numpy as np

import pandas
file = pandas.read_csv('Problem82.txt', header=None)
print(file)
data = []
file.values.tolist()

file = np.array(file)
file = np.transpose(file)
Path_Length = [0]*len(file[0])
for row in file:
    New_Length = [0]*len(row)
    for location in range(len(row)):
        # print('a')

        Row_Check = [Path_Length[a]+sum(row[location:a+1])+sum(row[a:location+1]) for a in range(len(row))]
        Row_Check[location] = Path_Length[location]+row[location]
        New_Length[location] = min(Row_Check)
        
    # print(Path_Length)
    Path_Length = [a for a in New_Length]
    # print(Path_Length)
    # print(min(Path_Length))
    # print(row)
    # input()
    
print(min(Path_Length))