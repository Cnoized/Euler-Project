# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 97

def Times2(Number):
    Number = (Number*2)%10000000000
    return Number
N=0
A=0
Number = 1
while N<7830457:
    N+=1
    Number = Times2(Number)


    # if A>10000:
    #     A-=10000
    #     print(Number, 'and', N)
    # else:
    #     A+=1
print(Number, 'and', N)
P_Number = (28433*Number+1)%10000000000
print('Last ten digits are', P_Number)