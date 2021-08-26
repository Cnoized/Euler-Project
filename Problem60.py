# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 60

#Prime Pair Sets
# import math
from Primes import GeneratePrimes
from Primes import PrimeCheck
P = [2,3]
# Answer = []
# Pairs = set()
# alpha = 0
# base = 2
# while Answer == []:
#     alpha+=1

#     P = GeneratePrimes(10**base,mode='Num',P=P)
#     if P[alpha]>10**(math.floor(base/2)):
#         base+=1
#         P=list(set(P))
#         P.sort()
#     for n in range(alpha-1):
#         print(P[n],P[alpha-1])
#         print(int(str(P[n])+str(P[alpha-1])))
#         if int(str(P[n])+str(P[alpha-1])) in P and int(str(P[alpha-1])+str(P[n])) in P:
#             Pairs.add((P[n],P[alpha-1]))
#             Pairs.add((P[alpha-1],P[n]))
#             print(set({P[n],P[alpha-1]}))
#         elif int(str(P[n])+str(P[alpha-1]))>max(P) or int(str(P[alpha-1])+str(P[n]))>max(P):
#             Answer = False
#             break
        
#         # input()
#     print(len(P))
#     print(max(P))
    
# print(Answer)
alpha = 5
P=GeneratePrimes(10000,mode='Num',P=P)
Pairs = []
for n in P:
    while 10**(len(str(n))+3)>len(P):
        alpha += 1
        P=GeneratePrimes(10**alpha,mode='Num',P=P)
    if PrimeCheck(int(str(n)+'3'))+PrimeCheck(int('3'+str(n)))==2:
        if PrimeCheck(int(str(n)+'7'))+PrimeCheck(int('7'+str(n)))==2:
            if PrimeCheck(int(str(n)+'109'))+PrimeCheck(int('109'+str(n)))==2:
                if PrimeCheck(int(str(n)+'673'))+PrimeCheck(int('673'+str(n)))==2:
                    print(n)
    
            Pairs.append([P[n],P[alpha-1]])
            Pairs.add((P[alpha-1],P[n]))
            print(set({P[n],P[alpha-1]}))
        elif int(str(P[n])+str(P[alpha-1]))>max(P) or int(str(P[alpha-1])+str(P[n]))>max(P):
            Answer = False
            break