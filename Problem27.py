# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 27

import math
P_L = []
n_max =0
g=0
for a in range(-1000,1001):
    if a>20*g-1000:
        print(g,'/100')
        g+=5
    for b in range(-1000,1001):
        # print(b)
        prime = 0
        n=0
        while prime == 0:
            # print(n**2+a*n+b)
            for i in range(2,math.floor(math.sqrt(abs(n**2+a*n+b)))+1):
                # print(i)
                if (n**2+a*n+b)%i == 0:
                    prime = 1
                    # print('not prime')
                # print(prime)
            n+=1
            # print(n)
        if n>n_max:
            P_L=[a,b,n]
            n_max=n
            print(P_L)
print('a: ', P_L[0])
print('b: ', P_L[1])
print('The product of a and b is: ',P_L[0]*P_L[1])