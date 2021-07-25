# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 28
import time
start_time=time.time()
i = 1
n=0
m=1
P = []
while n<500:
    n+=1
    for j in range(4):
        m+=2*n
        i+=m  
print(i)
print("--- %s seconds ---" % (time.time() - start_time))