# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 17
from num2words import num2words
Numbers = []
Words = []
L=0
for n in range(1,1001):
    word = num2words(n)
    print(word)
    word = word.replace(" ","").replace("-","")
    print(len(word))
    # print(word)
    Words.append(word)
    Numbers.append(len(word))
    L += len(word)
    
print(L)