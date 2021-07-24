# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 7

# import numpy as np
import math

Primes = [2]
    
n=3
while len(Primes)<10001:
    Root = math.sqrt(n)
    Root = math.floor(Root)
    print(Root)
    Dead = 0
    while Root>1:
        
        if n%Root == 0:
            Dead = 1
        Root -= 1
    if Dead != 1:
        Primes.append(n)
        print(n)
    n += 1
print('^^^ This is the 10001th prime. ^^^')