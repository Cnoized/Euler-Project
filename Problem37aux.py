# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 21:43:03 2021

@author: Cnoized
"""

P = [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
print(sum(P))
a = str(123456789)
for i in range(len(a)):
    print(a[:i+1])
    print(a[i:])