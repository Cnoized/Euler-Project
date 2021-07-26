# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 53
import math
Million = 0
for n in range(1,101):
    for r in range(0,n):
        if math.comb(n,r)>10**6:
            Million += 1
print(Million)