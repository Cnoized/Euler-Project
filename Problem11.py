# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 11
import pandas
file = pandas.read_csv('Problem11.csv', header=None)
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
upper = 0
for i in range(17):
    for j in range(17):
        num1 = 1
        num2 = 1
        num3 = 1
        num4 = 1
        for k in range(4):
            num1 = num1*data[i][j+k]
            num2 = num2*data[i+k][j]
            num3 = num3*data[i+k][j+k]
            num4 = num4*data[i+k][19-j-k]
            # print(j+k)
        if max(num1,num2,num3,num4) > upper:
            upper = max(num1,num2,num3,num4)
            print(upper)
            print(i,j)
print(data[6:6+k][15:15+k])