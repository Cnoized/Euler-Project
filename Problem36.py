# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 36
Pal = []
for n in range(1,1000):
    S = str(n)+str(n)[::-1]
    print(S)
    if int(S)%2 == 1:
        Pal.append(int(S))
    D = str(n)[:-1]+str(n)[::-1]
    print(D)
    if int(D)%2 == 1:
        Pal.append(int(D))
Bi = []
Dec = []
for p in Pal:
    d = p
    b = []
    while p>0:
        b.append(p%2)
        p=(p-p%2)/2
        
    if b == b[::-1]:
        Bi.append(b)
        Dec.append(d)
    else:
        print(b)
        print(b.reverse())
print(Bi)
print(Dec)
print(sum(Dec))