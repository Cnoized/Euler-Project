# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 72


import math
from sympy import totient as tot

MaxL=2
Maxd=5
number = 0
for d in range(2,1000001):
    number += tot(d)
    if d%100 == 0:
        print(d)
    
print(number)