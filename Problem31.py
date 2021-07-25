# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 31


L = [100,50,20,10,5,2]
P=[[200],[100],[50],[20],[10],[5],[2]]
Q=[]
Total = []
for n in range(100):
    for i in P:
        # path = [m for m in i]
        # if sum(i) == 200:
        #     Q.append([i])
        #     # print(Q)
            
        #     P.remove(i)
        # else:
        for j in L:
            if sum(i)+j<=200 and j<=min(i):
                i.append(j)
                alpha = [m for m in i]
                Q.append(alpha)
                i.pop()
    alpha = [m for m in P]
    Total.append(alpha)                
    P = [m for m in Q]
    Q = []
All=[]
for n in Total:
    for m in n:
        All.append(m)
print(len(All)+1)        
# # just another example that we should ignore the cents.
                
                
                