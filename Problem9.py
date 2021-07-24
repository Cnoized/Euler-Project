# -*- codiag: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 9
a=1
b=1

while a<1000:
    b = 1 
    a += 1
    # print(a)
    while b<1000:
        b += 1
        c = 1000 - b - a
        if c*c == (a*a) + (b*b):
            print(a)
            print(b)
            print(c)
            print('Answer is: ', a*b*c)