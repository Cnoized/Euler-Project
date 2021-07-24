# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 23

import math

answer = 0
n=1
Abundant = []
for a in range(1,29000):
    divisors = set()
    for i in range(2,math.floor(math.sqrt(a))+1):
        if a%i == 0:
            # print(a)
            # print(a/i)
            divisors.add(i)
            divisors.add(a/i)
    if sum(divisors)>a:
        print(a)
        print(divisors)
        Abundant.append(a)
T = set(range(1,29000))      
print(T)
print(Abundant)
for n in Abundant:
    for m in Abundant:
        T.discard(n+m)

print(sum(T))