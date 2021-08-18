# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 57

# #iterations of 1/2 to reach sqrt(2).

a = 3
b = 2
alpha = 0
for n in range(1,1000):
    c = a+2*b
    d = a+b
    a = c
    b = d
    if len(str(a))>len(str(b)):
        alpha += 1
print(alpha)
    