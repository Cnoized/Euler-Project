# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 50

import math
Answer = []
n = 3
P = [2,3]

while n<1000000:
    n+=2
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
print(len(P))
l = 511

for n in range(len(P)):
    a = 0
    b = 0
    i = 0
    # print(n)
    while P[a+i]<P[n]/l and b != P[n]:
        b = 0
        while b < P[n]:                
            
            b += P[a+i]   
            a += 1
            if b == P[n] and a>l:
                l = a
                Answer = [b,n,a,i]
                print(P[i:i+l+1])
                print(l)
            
        a = 0        
        i += 1
print(Answer) 