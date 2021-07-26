# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 35

import math

P=[2]
for n in range(3,1000001):
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
print(P)
C=[]
for p in P:
    Num = str(p)   
    prime = 0
    for i in range(10):
        Test = Num[i:]+Num[:i]
        Test = int(Test)        
        m = 0
        q=1
        while q<math.sqrt(Test) and prime == 0:
            q = P[m]
            m+=1
            if Test%q == 0:
                prime = 1
    if prime == 0:
        C.append(p)
print(C)
# # Didn't catch 2 as a circular prime, but we just need to notice that and include it in the final count.