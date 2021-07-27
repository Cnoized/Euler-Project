# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 55

L = []
for n in range(1,10000):
    print(n)
    m=0
    while m<50:
        m+=1
        n+=int(str(n)[::-1])
        # print(n)
        if str(n) == str(n)[::-1]:
            break
            print(n)
    if m >= 50:
        L.append(n)