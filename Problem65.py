# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 65

List_e = [2,1]

for n in range(1,34):
    List_e = List_e+[2*n,1,1]
print(List_e)
print(len(List_e))
List_e.pop()
print(List_e)
print(len(List_e))
List_e.pop()
Numerator = 1
Denominator = 1
while List_e != []:
    NextValue = List_e.pop()
    Temp1 = NextValue*Denominator+Numerator
    Numerator = Denominator
    Denominator = Temp1
print('Numerator',Temp1,'Denominator',Numerator)
print((Numerator/Temp1)**(-1))
print('Total for numerator digit sum is ',sum([int(a) for a in str(Temp1)]))

    