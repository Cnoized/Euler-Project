# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:06:05 2021

@author: Cnoized
"""

# from itertools import permutations as perm

# Final = {
#     1 : [[1]],
#     89 : [[8,9]]
#     }

def DigitsSquare(Start,Number):
    # global Path
    NewNumber = sum([int(a)**2 for a in str(Number)])
    # NewNumber = [int(a) for a in str(DigitsSquared)]
    # Step = [int(a) for a in str(NewNumber)]
    if NewNumber in List1:
        List1.append(Start)
        return 1
    elif NewNumber in List89:
        List89.append(Start)
        return 89
    else:
        # Path = Path+list(perm(Step))
        return NewNumber
    
List1 = [1]
List89 = [89]


for index in range(1,648):
    Number = index
    # Path = list(perm([int(a) for a in str(Number)]))
    # if [int(a) for a in str(index)] not in Final[1] and [int(a) for a in str(index)] not in Final[89]:
    while Number != 1 and Number != 89:
        Number = DigitsSquare(index,Number)
    # if Number == 1:
    #     # for item in Path:
    #     #     if item not in Final[1]:
    #     #         Final[1].append(list(item))
    #     print(index,len(Final[1]))
    # if Number == 89:
    #     # for item in Path:
    #     #     if item not in Final[1]:
    #     #         Final[89].append(item)
    # if index%100000 == 0:
    print(index)

print('Total in List1', len(List1))
print('Total in List89', len(List89))
print('Total in both Lists', len(List1+List89))
Total1=0 
for index in range(1,10000001):
    if sum([int(a)**2 for a in str(index)]) in List1:
        Total1 += 1
print('Total ends in 1', Total1)
print('Total ends in 89',10000000-Total1)