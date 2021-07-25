# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 26

# import numpy as np
n=[]
R=[]
for d in range(1,1000):
    alpha = [1,9]
    i=0
    while alpha[-1] != alpha[-2]:
        i+=1
        alpha = [(10**(i*n))%d for n in range(95,100)]
        if alpha[-1] == alpha[-2]:
            R.append([d,i,alpha[-1]])
    print(i)
a,b,c = map(list,zip(*R))
# max(b)
print(max(b))    
# # I think this is a really computatinally expensive solution, but it gets the job done.  
