# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 10

import math

Primes = [2]
k=0
n=3
while n<2000001:
    Root = math.sqrt(n)
    Root = math.floor(Root)
    # print(Root)
    Dead = 0
    while Root>1:
        
        if n%Root == 0:
            Dead = 1
        Root -= 1
    if Dead != 1:
        Primes.append(n)
        # print(n)
    n += 1
    if n>k:
        k+=100000
        print(k/1000,'/',100)
Answer = sum(Primes)
# Answer = math.prod(Primes) #oops
print(Answer)