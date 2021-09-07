# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:41:35 2021

@author: Cnoized
"""

n=0
SquareSums = []
MaxSum = 1
def SquareAdd(Sequence,n):
    # print(Sequence)
    global SquareSums
    global MaxSum
    Squares = [i**2 for i in range(1,10)]
    if n<8:
        n+=1
        for index in Squares:
            # print(Sequence,index)
            SquareAdd(Sequence+[index],n)
    else:
        Total = sum(Sequence)
        if Total>MaxSum:
            MaxSum = Total
            print(MaxSum)
            # print(Total)

S = [i**2 for i in range(1,10)]
for value in S:
    print(S)
    SquareAdd([value],1)

print(len(SquareSums))
        