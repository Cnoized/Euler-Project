# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:27:48 2021

@author: Cnoized
"""

# L = [n for n in range(100,1000)]
R = [n for n in range(999,99,-1)]
# R.reverse()
# print(min(L))
# print(max(L))
print(R[0])
print(R[-1])
PalList = []
Answer = 0
for n in R:
    for m in R:
        Palindrome = n*m
        Alpha = Palindrome
        Values = []
        while Alpha>0:
            i = Alpha % 10
            Values.append(i)
            Alpha = (Alpha-i)/10
        if Values == Values[::-1]:
            print(Palindrome, ' = ', n, '*', m)
            PalList.append(Palindrome)
            if Palindrome > Answer:
                Answer = Palindrome
            print('Largest Palindrome so far is: ', Answer)
print('Max of PalList: ', max(PalList))
