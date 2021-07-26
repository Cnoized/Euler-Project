# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 37

# PD = [2,3,5,7]

import math
TP = []
P=[2,3,5,7]
for n in range(10,1000000):
    p=1
    prime = 0
    m = 0
    while p<math.sqrt(n) and prime == 0:
        p = P[m]
        m+=1
        if n%p == 0:
            prime = 1
    if prime == 0:
        P.append(n)
        a = str(n)
        for i in range(len(a)):
            # print(range(len(a)))
            # print(i)
            if P.count(int(a[:i+1])) == 0 or P.count(int(a[i:])) == 0:
                prime = 1
        if prime == 0:
            TP.append(n)
print(TP)