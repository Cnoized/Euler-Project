# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 44
import math
Pair = []
Penta = []
alpha = [1560090]
# # First D found already through running for a couple seconds.
Delta = []
for n in range(1,10000000):
    p = n*(3*n-1)/2
    for m in Delta:
        if int((math.sqrt(24*(p+2*m)+1)+1)/6) == (math.sqrt(24*(p+2*m)+1)+1)/6:
            if int((math.sqrt(24*(p+m)+1)+1)/6) == (math.sqrt(24*(p+m)+1)+1)/6:
                Pair.append([p,p+m,m])
                print([p,p+2*m,p+m,m])
                print('Answer is:', p)
                alpha.append(m)
    Penta.append(p)
    if p<=min(alpha):
        Delta.append(p)
            