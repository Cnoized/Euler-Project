# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 32
import math

L = [1,2,3,4,5,6,7,8,9]
P = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
Q = []
for n in range(8):
    Q=[]
    for i in P:
        for j in L:
            if i.count(j) == 0:
                i.append(j)
                alpha=[n for n in i]
                Q.append(alpha)
                i.pop()
    P = [a for a in Q]
print(len(P))
All = set()
for n in P:
    if n[0]*(n[1]*10**3+n[2]*10**2+n[3]*10+n[4])==n[5]*10**3+n[6]*10**2+n[7]*10+n[8]:
        All.add(n[5]*10**3+n[6]*10**2+n[7]*10+n[8])
        print(n[0],'*',(n[1]*10**3+n[2]*10**2+n[3]*10+n[4]),'==',n[5]*10**3+n[6]*10**2+n[7]*10+n[8])
    if (n[0]*10+n[1])*(n[2]*10**2+n[3]*10+n[4])==n[5]*10**3+n[6]*10**2+n[7]*10+n[8]:
        All.add(n[5]*10**3+n[6]*10**2+n[7]*10+n[8])
        print((n[0]*10+n[1]),'*',(n[2]*10**2+n[3]*10+n[4]),'==',n[5]*10**3+n[6]*10**2+n[7]*10+n[8])
print(len(All))
print(sum(All))