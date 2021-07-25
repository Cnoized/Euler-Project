# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 00:11:59 2021

@author: Cnoized
"""

import math

DF = [34,125,41068,1466,372970,81368,1,145,2,40585,1]

for N in DF:
    M=[int(a) for a in str(N)]
    S=[math.perm(i) for i in M]
    if N == sum(S):
        print(N)
# # Included this portion as a check on some of the outputs in a separate console. 