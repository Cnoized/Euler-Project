# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 71

import math

MaxL=2
Maxd=5

for d in range(8,1000001):
    L = math.floor(d*3/7)
    while math.gcd(L,d) != 1 and L != 0:
        L-=1
    if L/d>MaxL/Maxd:
        MaxL = L
        Maxd = d
        print(MaxL)
        print(Maxd)
        print(MaxL/Maxd)
        
    
