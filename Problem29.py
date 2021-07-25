# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 29

N = set()
print([j for j in range(2,100)])
for a in range(2,101):
    for b in range(2,101):
        N.add(a**b)
print(len(N))