# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 48
N = 0
for n in range(1,1001):
    N += n**n
    # print(n**n)
print(N)
print('The last ten digits are:')
print(str(N)[-10:])