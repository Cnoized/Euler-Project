# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 41

import math
for m in range(3,11):    
    L = [a for a in range(1,m)]
    P = [[a] for a in range(1,m)]
    Q = []
    for n in range(m-2):
        Q=[]
        for i in P:
            for j in L:
                if i.count(j) == 0:
                    # alpha=[n for n in j]
                    # print('Path before: ',Path)
                    i.append(j)
                    # print('Arcs_s before: ',Arcs_S)
                    # print('Path after: ',Path)
                    alpha=[n for n in i]
                    Q.append(alpha)
                    #print('Path_Next after: ', Path_Next)
                    i.pop()
        P = [a for a in Q]
        print(n)
    
    P=[2,3,5,7]
    for n in range(10,int(math.sqrt(int(''.join([str(a) for a in max(Q)]))))):
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
    alpha = 0
    beta = 0
    for n in Q:
        alpha += 1
        n = int(''.join([str(a) for a in n]))
        # print(n)
        prime = 1
        for i in P:        
            if n%i == 0:
                # print(i)
                prime = 0
        if prime == 1:
            p_max = n
            print(p_max)
        if alpha > len(Q)*beta/100:
            beta += 1
            print(beta,'/100')
            
# #Stops producing prime numbers after 8s are introduced. Largest number given as prime was 7652413. Program still runs through next few levels.