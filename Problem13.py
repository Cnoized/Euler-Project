# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 13

import pandas
file = pandas.read_csv('Problem13.csv', header=None)
print(file)
data = []
file.values.tolist()
for n in file.values:
    print(n)
    # print(str(n))
    # n=str(n[0]).split(' ')
    # print(n)
    n = int(n)
    data.append(n)
print(data)
print('The first ten digits of: ', sum(data))
