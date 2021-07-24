# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 12
import math
#produce the triangle numbers and then check for the number of divisors.
answer = 0 
n=10
L=1
while answer == 0:
    n += 1
    divisors = []
    a=sum(range(n))
    # print(a)
    for i in range(1,math.floor(math.sqrt(a+1))):
        if a%i == 0:
            divisors.append(i)
    if len(divisors)>L:
        print(a)
        maxD=[n for n in divisors]
        L=len(maxD)
        print(L)
    if len(divisors)>250:
        print(n, ' has over 500 divisors.')
        break