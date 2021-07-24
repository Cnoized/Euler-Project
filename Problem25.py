# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 25
L=0
F = [1,1]
while L<1000:
    F.append(F[-1]+F[-2])
    L = len([int(a) for a in str(F[-1])])
print(F[-1])

print(L)