# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 52
from time import time

start1 = time()
answer = 0
n = 100000
while answer == 0:
    n+=1
    if len(set(str(n)))!=len(str(n)):
        continue
    z = set(str(n))
    a = set(str(2*n))
    b = set(str(3*n))
    c = set(str(4*n))
    d = set(str(5*n))
    e = set(str(6*n))
    if z==a and z==b and z==c and z==d and z==e:
        print(n)
        answer = n
end1 = time()
time1 = end1 - start1
print(time1, 'second(s)')