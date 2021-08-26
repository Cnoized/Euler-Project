# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 62
from time import time
from itertools import permutations
import numpy as np
P_List = []

start1 = time()



def CubicPermutations(Times):
    Number = 0
    N = 2
    # Cubes = GenerateCubes(5)
    
    while Number < Times:
        N+=1

        Number = 0

        Cube = sorted([int(a) for a in str(N**3)])
        P_List.append([Cube])
        Check = P_List.count([Cube])
        # if Check > 1:
            # print(Check)
        if Check > Number:
            Number = Check
    for Base in range(N):
        Cube2 = sorted([int(a) for a in str(Base**3)])
        if Cube2 == Cube:
            print(Base,'is the smallest base for which its cube has 5 permutations which are also cubes.',Base**3,Cube2)
        # print(P_List)
        # print(Cubes)
        # input()
        

        # for a in P_List:

        #     if a in Cubes and a not in P_Int:
        #         Number += 1
        #         print(N,Number)
        #     P_Int.append(a)
    # print(P_List)
    # print(N)
    return N


def GenerateCubes(Number):
    Alpha=1
    Cubes = []
    Value = (10**len(str(Number)))
    while Alpha < Value:
        Cubes.append([a for a in str(Alpha**3)])
        Alpha+=1
    # print(len(Cubes))
    # print(len(max(Cubes)))
    return Cubes

LookingFor = 5
Answer = CubicPermutations(LookingFor)
print(Answer, 'at', LookingFor)

end1 = time()

print(end1-start1)