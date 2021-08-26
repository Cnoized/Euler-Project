# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 78

# import math

# def SumCombinations(Goal):
#     Final_Ways = []
#     Ways_All = [[a] for a in range(Goal)]
#     New_Ways = []
#     Percent = 0
#     while Ways_All != []:
#         for element in Ways_All:
#             # print(element)
#             Total_element = sum(element)
#             if element != []:
#                 Min_element=min(element)
#             else:
#                 Min_element=0
#             for value in range(1,min(Min_element,Goal-Total_element)+1):
#                 New_Ways.append(element+[value])
#             if sum(element) == Goal:
#                 Final_Ways.append(element)
#         Check = math.floor(len(Final_Ways)*100/(len(Final_Ways+New_Ways)+1))
#         if Check>Percent:
#             Percent = Check
#             print(Percent, '/ 100')
#         Ways_All = [a for a in New_Ways]
#         New_Ways = []  
#     print(len(Final_Ways))
#     return len(Final_Ways)


# New_List = [[1]]            
# def SumCombinations(Goal):
#     New_List = [[1]]
#     for run in range(1,Goal):
#         print(run,len(New_List))
#         Total_List = [a for a in New_List]
#         New_List = []
#         for element in Total_List:
#             for value in set(element):
#                 New_element = [a for a in element]
#                 New_element[element.index(value)]+=1
#                 if New_element not in New_List:
#                     New_List.append(New_element)
#             if element+[1] not in New_List:
#                 New_List.append(element+[1])
#     # print(len(New_List),len(Total_List),sum(New_List[0]),print(New_List))
#     return len(New_List)

# SumCombinations(5)
# print(New_List)
# SumCombinations(100)

## Above code works, but it takes forever to run. Would compute to 100th value and output the answer.

def pentagonal_number(k):
    return int(k*(3*k-1) / 2)

def compute_partitions():
    partitions = [1]
    n=0
    while partitions[-1]%1000000 != 0:
        n+=1
        partitions.append(0)
        for k in range(1,n+1):
            coeff = (-1)**(k+1)
            for t in [pentagonal_number(k), pentagonal_number(-k)]:
                if (n-t) >= 0:
                    partitions[n] = partitions[n] + coeff*partitions[n-t]
        print(partitions[-1],n)
    return partitions[-1]

# n=1
# answer = 1
# while answer%1000000 != 0:
#     n+=1
#     answer = compute_partitions(n)
#     print(answer, n)
# print(answer,n)
answer = compute_partitions()
##Variable 
print(answer)

##Answer will be the same as the number of partitions minus 1. Last value in the printed list minus 1 is value of how many ways 100 can be divided in to two or more numbers. This is because the number of partitions includes the number without any subdivisions. So we subtract that case from the total number of partitions.
