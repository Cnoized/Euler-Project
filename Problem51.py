# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 51
import math

Answer = []
n = 3
P = [2,3]
PB = []
PC = []
# from Primes import GeneratePrimes
# P = GeneratePrimes(10000)
while n<1000000:
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
        if len(str(n)) == 5:
            PB.append(n)
        if len(str(n)) == 6:
            PC.append(n)
        # print(n)
alpha_min = 10
# for n in PB:
#     if n%5 == 0:
#         print(n)
PD = []
# for n in PB:
#     n = str(n)
Completed = []
print(len(PC))
# for Viable in PC:
#     V = str(Viable)
#     if '0' not in V and '1' not in V and '2' not in V:
#         PC.remove(Viable)
# print(len(PC))
b = 0
c = 1
d = 2

# for i in range(10):
#     a = str(100109)
#     a = a[:b]+str(i)+a[b+1:]
#     a = a[:c]+str(i)+a[c+1:]
#     a = a[:d]+str(i)+a[d+1:]
#     a = int(a)
#     if a in PD:
#         print(a)
Candidates = 0
for b in range(10):
    for c in range(10):
        for d in [1,3,7,9]:
            Full_String = 'aaaaa'
            for n in range(len(Full_String)-1):
                for m in range(n,len(Full_String)):
                    a = Full_String
                    a = a[:n]+str(b)+a[n+1:]
                    a = a[:m]+str(c)+a[m+1:]
                    a = a+str(d)
                    alpha = 0
                    for e in range(10,0,-1):
                        # print(a)
                        
                        Interger = a.replace('a',str(e))
                        # print(a)
                        if int(Interger) not in P:
                            alpha += 1
                        if alpha == alpha_min+1:
                            break
                    if alpha<alpha_min:
                        alpha_min = alpha
                        n_min = int(Interger)
                        Candidates=int(Interger)
                    if alpha<=alpha_min:
                        print(alpha,Interger,a)
                        
print(Candidates)


# for b in range(0,len(str(PC[0]))-1):
#     for c in range(0,len(str(PC[0]))-1):
#         for d in range(0,len(str(PC[0]))-1):
#             for e in range(0,len(str(PC[0]))-1):
#                 if set([b,c,d,e]) in Completed or len(set([b,c,d,e]))<3:
#                     continue
#                 Completed.append(set([b,c,d,e]))
#                 PD = [zeta for zeta in PC]
#                 for n in PD:
#                     alpha = 0
#                     # print(b,c)
#                     # input()
#                     for i in range(10):
                        
#                         # print(i)
#                         a = str(n)
#                         a = a[:b]+str(i)+a[b+1:]
#                         a = a[:c]+str(i)+a[c+1:]
#                         a = a[:d]+str(i)+a[d+1:]
#                         a = a[:e]+str(i)+a[e+1:]
#                         # print(a)
#                         a = int(a)
#                         # if a in PD:
#                         #     PD.remove(a)
#                         if a not in PD:
#                             alpha += 1
#                         else:
#                             # print('alpha')
#                             print(a)
#                         if alpha == alpha_min+1:
                            
#                             # print('break')
#                             break
#                     # print(alpha)    
#                     if alpha<alpha_min:
#                         alpha_min = alpha
#                         n_min = n
#                     if alpha<=alpha_min:
#                         print(alpha,n,set([b,c,d,e]))
# print(alpha_min,n_min)
                    
        