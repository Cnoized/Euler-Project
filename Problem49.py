# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 49
import math
answer = 0
n = 3
P = [2,3]
R = []
P4 = []
Ans = []
while n<10000:
    n+=2
    p=1
    prime = 0
    m = 0
    while p<math.sqrt(n) and prime == 0:
        p = P[m]
        m+=1
        if n%p == 0:
            prime = 1
    if prime == 0:
        P.append(n)
        if len(str(n)) == 4:
            P4.append(n)
print(len(P4))
            # A = [a for a in str(n)]
            # L = [a for a in A]
C = set()

for B in P4:
    # print(B)
    A = [a for a in str(B)]
    # print(A)
    L = [a for a in str(B)]
    for z in range(3):
        Q=[]
        for i in A:
            for j in L:
                if i.count(j) < str(B).count(j):
                    # alpha=[n for n in j]
                    # print('Path before: ',Path)
                    i+=j
                    # print('Arcs_s before: ',Arcs_S)
                    # print('Path after: ',Path)
                    alpha=[k for k in i]
                    Q.append(alpha)
                    #print('Path_Next after: ', Path_Next)
                    i = i[:-1]
            # print(i)        
        A = [a for a in Q]
    D = set()
    for a in A:
        # print('a',a)
        a =''.join([str(x) for x in a])
        # print('a',a)
        a = int(a)
        if a in P4:
            D.add(a)
    D = list(D)
    if len(D)>=3:
        # print(D)        
        for a in D:
            for b in D:
                # print('a',a,type(a))
                # print('b',b,type(b))
                if a > b and 2*a-b in D and b not in Ans:
                    print(b,a,2*a-b)
                    Ans.append(b)
                    # answer = [a,b,2*a-b]
            # if a in P4:
            #     C.add(a)
# print(C)    
# C = list(C)
# print(C)
# print(len(C))

# # This is a really ugly program with some inefficiencies, but it works, and it is realtively fast so it should be alright.    
    
            #     # print('A', A)
            # B = []
            
            #     if a not in P:
            #         B.remove(a)
            #     elif len(str(a))<4:
            #         B.remove(a)
            # for a in B:
            #     for b in B:
            #         # print('a',a,type(a))
            #         # print('b',b,type(b))
            #         if a > b and 2*a-b in B:
            #             print(a,b,2*a-b)
            #             # answer = [a,b,2*a-b]
                        
    # if n >10000:
    #     answer = 1
        