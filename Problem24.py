# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 24

L = [0,1,2,3,4,5,6,7,8,9]
P = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
Q = []
for n in range(9):
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
print(P[999999])
# # Answer should be [2, 7, 8, 3, 9, 1, 5, 4, 6, 0] or 2783915460.