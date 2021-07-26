# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 46

import math

answer = 0
n=1
P = [2]
N = [n]
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
        for a in range(1,math.floor(math.sqrt(n/2))+1):
            num = n-2*a**2
            if num in P:
                prime = num
        if prime == 1:
            answer = n
            print(n,prime,(n-prime)/2)
                
