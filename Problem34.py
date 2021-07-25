# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 34
import math
DF = []
for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    for f in range(0,10):
                        for g in range(0,10):
                            M=[a,b,c,d,e,f,g]
                            for n in range(7):                                
                                N=[str(i) for i in M]
                                N=int(''.join(N))
                                S=[math.perm(i) for i in M]
                                if N == sum(S) and N not in DF:
                                    print(N)
                                    DF.append(N)
                                M.pop()
# print(math.perm(0))

for N in DF:
    M=[int(a) for a in str(N)]
    S=[math.perm(i) for i in M]
    if N == sum(S):
        print(N)
        
# # This was a rather computationally expensive approach. It could be simplified a little bit.