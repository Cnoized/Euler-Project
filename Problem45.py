# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 45

import math

n = 143

T = False
P = False
H = False

while T&H&P == False:
    n+=1
    a = n*(2*n-1)
    T = int((math.sqrt(8*(a)+1)-1)/2) == (math.sqrt(8*(a)+1)-1)/2
    H = int((math.sqrt(8*(a)+1)+1)/4) == (math.sqrt(8*(a)+1)+1)/4
    P = int((math.sqrt(24*(a)+1)+1)/6) == (math.sqrt(24*(a)+1)+1)/6
print(a,T,H,P)