# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 14
n=1
Max_S=0
while n < 1000000:
    n+=1
    a=n
    steps=0
    while a != 1:
        if a%2 == 0:
            a=a/2
        else:
            a=a*3+1
        steps+=1
    if steps>Max_S:
        Max_S=steps
        print(Max_S)
        print(n)