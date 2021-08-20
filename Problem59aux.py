# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:27:29 2021

@author: Cnoized
"""


import pandas
file = pandas.read_csv('Problem59.csv', header=None)
print(file)
data = []
file.values.tolist()
for n in file.values:
    print(n)
    print(str(n))
    
i=101
j=120
k=112
Valid0 = 0
Valid1 = 0
Valid2 = 0
p=0
while p<len(n):
    if p%3 == 0:
        n[p]=n[p]^i
        if n[p] in range(97,123) or n[p] in range(65,92) or n[p] == 32 or n[p] == 44 or n[p] == 46:
            Valid0+=1
    elif p%3 == 1:
        n[p]=n[p]^j
        if n[p] in range(97,123) or n[p] in range(65,92) or n[p] == 32 or n[p] == 44 or n[p] == 46:
            Valid1+=1
    elif p%3 == 2:
        n[p]=n[p]^k
        if n[p] in range(97,123) or n[p] in range(65,92) or n[p] == 32 or n[p] == 44 or n[p] == 46:
            Valid2+=1
    p+=1
m=[]
for a in n:
    
    m.append(chr(a))
print(m)
TotalValid = 0
for a in range(len(n)):
    if n[a] in range(97,123) or n[a] in range(65,92) or n[a] == 32 or n[a] == 44 or n[a] == 46:
        TotalValid+=1
print(TotalValid)
print(len(n))
print(Valid0,Valid1,Valid2)
        # ord('t')
print(''.join([chr(a) for a in n]))
print(sum([a for a in n]))