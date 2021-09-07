# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 92

from itertools import permutations as perm

Final = {
    1 : [[1]],
    89 : [[8,9]]
    }

def DigitsSquare(Start,Number):
    global Path
    NewNumber = sum([int(a)**2 for a in str(Number)])
    # NewNumber = [int(a) for a in str(DigitsSquared)]
    Step = [int(a) for a in str(NewNumber)]
    if set(Step) in Final[1]:
        # List1.append(Start)
        return 1
    elif set(Step) in Final[89]:
        # List89.append(Start)
        return 89
    else:
        Path = Path+list(perm(Step))
        return NewNumber
    
List1 = [1]
List89 = [89]


for index in range(1,10000001):
    Number = index
    Path = list(perm([int(a) for a in str(Number)]))
    if [int(a) for a in str(index)] not in Final[1] and [int(a) for a in str(index)] not in Final[89]:
        while Number != 1 and Number != 89:
            Number = DigitsSquare(index,Number)
        if Number == 1:
            for item in Path:
                if item not in Final[1]:
                    Final[1].append(list(item))
            print(index,len(Final[1]))
        if Number == 89:
            for item in Path:
                if item not in Final[1]:
                    Final[89].append(item)
    if index%100000 == 0:
        print(index)
print(len(Final[1]))
print(len(Final[89]))
print(len(Final[1]+Final[89]))