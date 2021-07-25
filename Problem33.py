# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 33

import math
A=[]
C=[]
Frac = []
L = 1
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if (10*a+b)/(10*b+c)==a/c and a != b != c:
                print(10*a+b,'/',10*b+c,'=',a/c)
                Frac.append(a/c)
                L = L*(a/c)
                A.append(a)
                C.append(c)
print(math.prod(Frac))
print(L)
print(math.prod(A),'/',math.prod(C))
# 8/800 reduces to 1/100 so the demoninator comes out as 100.