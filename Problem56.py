# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 56
c_max = 0
for a in range(1,100):
    for b in range(1,100):
        c = sum([int(a) for a in str(a**b)])
        if c>c_max:
            c_max = c
            print(c)