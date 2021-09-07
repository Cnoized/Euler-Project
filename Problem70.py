# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 70

import math
from sympy import totient as tot
from itertools import permutations as perm
PermMin = 87109/79180
Num = 0
R = [10**7+2-n for n in range(2,10**7)]
for n in range(2,10**7):
    Ratio = n/tot(n)
    if Ratio<PermMin:
        # print(n)
        Rest = [int(a) for a in str(n)]
        for element in [int(a) for a in str(tot(n))]:
            if element in Rest:
                Rest.remove(element)
            else:
                break
        if Rest == []:
            PermMin = Ratio
            Num = n
            print(n,'and', PermMin)
            
            