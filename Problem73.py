# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 73



import math

MaxL=2
Maxd=5
number = 0
for d in range(2,12001):
    for n in range(1,d):
        if n/d<1/2 and n/d>1/3:
            if math.gcd(n,d) == 1:
                number += 1
    if d%100 == 0:
        print(d)
print(number)
