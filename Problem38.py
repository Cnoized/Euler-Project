# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 38
Pal = []
# for a in range(1000,10000):
#     b = [int(n) for n in str(a)+str(2*a)]
#     Yes = 0
#     No = 0
#     for n in range(1,9):
#         if b.count(n) >= 1:
#             Yes = 1
#         else:
#             No = 1
#     if No == 0:
#         Pal.append(a)

for a in range(1,10000):
    i=0
    b=[]
    while len(b)<9:
        i+=1
        for n in str(i*a):
            b.append(int(n))
    Yes = 0
    No = 0
    if len(b) == 9:
        # print(b)
        for n in range(1,9):
            if b.count(n) >= 1:
                Yes = 1
            else:
                No = 1
        if No == 0:
            Pal.append(a)
b_max = 0
for a in Pal:
    i=0
    b=[]
    while len(b)<9:
        i+=1
        b+=str(i*a)
    b = ''.join(b)
    if int(b)>int(b_max):
        b_max = b
        print(a,b)
# print(Pal)


# # I actually did this one by hand, but it still was easy enough to make the program to find it. I had an idea it was something with 4 digits because the largest 3 digit numbers were in the 300s, and the largest single digit number was 9 and it would only have around 919 million as it's upper bound. Almost any viable 4 digit number starting with 9 would be better. Luckly I found one, and this program confirmed it.