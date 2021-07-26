# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 39
import math
L = []
for a in range(1,1000):
    for b in range(1,1000):
        c = math.sqrt(a**2+b**2)
        if c == int(c) and a+b+c<1000:
            print(a,b,c,a+b+c)
            L.append(a+b+c)
d_max = 0
for n in L:
    d = L.count(n)
    if d>d_max:
        d_max = d
print(d,n)
            
            