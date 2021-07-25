# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 30
Fifths = []
for n in range(2,1000000):
    number = [int(a)**5 for a in str(n)]
    if sum(number) == n:
        Fifths.append(n)
print(sum(Fifths))