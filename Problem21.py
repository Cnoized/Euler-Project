# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 21

import math

answer = 0 
L=1
# Data1 = []
# Data2 = []
Amical = set()
for n in range(1,10001):
    divisors = []
    # print(a)
    for i in range(1,n):
        if n%i == 0:
            divisors.append(i)
    TD=sum(divisors)
    divisors = []
    for i in range(1,TD):
        if TD%i == 0:
            divisors.append(i)
    SD=sum(divisors)
    if SD == n:
        print(n, TD)
        if n == TD:
            print('not added')
        else:
            Amical.add(n)
            Amical.add(TD)
            print('added')

# Data3 = [Data2.index(n) for n in Data1]
    

print(sum(Amical), 'is the total of all amical pairs.')