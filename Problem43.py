# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 43
m=10
L = [a for a in range(0,m)]
P = [[a] for a in range(0,m)]
Q = []
primes = [1,1,2,3,5,7,11,13,17]
for n in range(m-1):
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
                print(alpha[-3:])
                if int(''.join([str(m) for m in alpha[-3:]]))%(primes[n]) == 0:
                    Q.append(alpha)
                    print(alpha[-3:])
                #print('Path_Next after: ', Path_Next)
                i.pop()
    P = [a for a in Q]
    
        
    # print(P)
    print(n)
W=[]
for a in Q:
    W.append(int(''.join([str(m) for m in a])))   
print(sum(W))