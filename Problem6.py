# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:46:43 2021

@author: Cnoized
"""

Natural = range(1,101)
N = sum(Natural)
print(N)
print(N*N)
Mul = [a*a for a in Natural]
M = sum(Mul)
print(M)
print('Answer: ', N*N-M)

