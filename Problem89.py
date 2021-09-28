# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 89
from time import time

start1 = time()

import pandas
file = pandas.read_csv('Problem89.txt', header=None)
print(file)
data = []
file.values.tolist()
print(file)

Roman = []

Is = []
Vs = []
Xs = []
Ls = []
Cs = []
Ds = []
Ms = []
Count = 0



for entry in file.values.tolist():
    
    # L_temp = [element for element in str(entry)]
    entry = str(entry)
    if entry.find('VIIII') != -1:
        Count += 3
    elif entry.find('IIII') != -1:
        Count += 2
    # elif entry.find('VIII') != -1:
    #     Count += 1
    if entry.find('LXXXX') != -1:
        Count += 3
    elif entry.find('XXXX') != -1:
        Count += 2
    # elif entry.find('LXXX') != -1:
    #     Count += 1
    if entry.find('DCCCC') != -1:
        Count += 3
    elif entry.find('CCCC') != -1:
        Count += 2
    # elif entry.find('DCCC') != -1:
    #     Count += 1
    #entry.find('VIII','IIX')
    #entry.find('LXXX','XXC')
    #
    # Roman.append(L_temp)
    # Is.append(L_temp.count('I'))
    # Vs.append(L_temp.count('V'))
    # Xs.append(L_temp.count('X'))
    # Ls.append(L_temp.count('L'))
    # Cs.append(L_temp.count('C'))
    # Ds.append(L_temp.count('D'))
    # Ms.append(L_temp.count('M'))
    
# print(max(Is))
# print(max(Vs))
# print(max(Xs))
# print(max(Ls))
# print(max(Cs))
# print(max(Ds))
# print(max(Ms))

print(Count)
end1 = time()-start1
print(end1)
