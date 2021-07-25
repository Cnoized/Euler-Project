# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:43:24 2021

@author: Cnoized
"""

#This is a file which is supplementary to show what is going on in the other program, and to confirm it gets the right answer.

alpha=[]
i=982
d=983
for n in range(1,1000):
    alpha.append((10**(i*n))%d)
    print(n)
print(alpha)
print('These are the repeating remainders every 982.')

alpha=[]
d=983
for i in range(1,1000):
    alpha.append((10**(i))%d)
    # print(i)
print(alpha)
print('Remainders repeat at 983nd index.')
