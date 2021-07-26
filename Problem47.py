# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 47

import math

answer = 0
n=3
P = [2,3]
N = [n]
L = []

while answer == 0:
    n+=2
    N.append(n)
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
    else:
        if n-2 not in P:
            L = []
            for a in range(n-3,n+2):
                m = 0
                i = a
                A = []
                while a>1:
                    p = P[m]                    
                    if a%p == 0:
                        a = a/p
                        A.append(p) 
                    else:
                        m+=1
                # print(A)
                L.append(len(set(A)))
            if L.count(4) >= 4:
                 # print(L)
                 # print(n)
                 if L[0] != 4:
                     answer = n-2
                 if L[4] != 4:
                     answer = n-3
print(answer)                    
