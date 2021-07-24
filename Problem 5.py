# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:04:25 2021

@author: Cnoized
"""
import numpy as np


# math=range(1,21)
# print(math.lcm())
# # If only I had Python 3.9 on Spyder then .lcm() would be a one line solution to this problem.
Primes = []
for n in range(1,21):
    if n>1:
        a = n-1
    else:
        a=10
    check = []
    
    while a>0:

        print(n%a)
        check.append(n%a)
        a -= 1
    if check:
        if check.count(0)==1:
            Primes.append(n)
    
print(Primes)
Primes.pop(0)
print(Primes)
Factors = []
for n in Primes:
    a = 20
    i=0
    while a/n>=1:
        i += 1
        a = a/n
        Factors.append(n)
    # Factors.append(i)
print(Factors)    


# multiples = [a^b for a,b in zip(Primes,Factors)]
# print(multiples)
print(np.prod(Factors))
