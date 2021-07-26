# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 40
a=''
for n in range(1,1000000):
    a += str(n)
i=1
T = 1
for n in range(7):
    print(a[i-1])
    T = T*int(a[i-1])
    i=i*10
print('T',T)