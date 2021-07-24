# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 16
import math
L = [2]*1000
twos=math.prod(L)
S = [int(a) for a in str(twos)]
print(sum(S))