# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 63
A_L = []
Total = 9
#Start with 9 for the first 9 positive intergers with the first power. Iterate through integers 2 to 9 and their powers above 1. Stop when reaching a point where the length of the power is larger than the power itself. Nothing beyond 9 can have a power in this format because the integer will always have more digits than the power number.
for n in range(2,10):
    N=2
    Answer = str(n**N)


    while len(Answer) == N:
        Total += 1
        A_L.append([n**N,n,N])
        N+=1
        Answer = str(n**N)
        if N>200:
            break
        print(N,n**N)
    print(n)
print(Total)
print(A_L)
print(len(A_L))