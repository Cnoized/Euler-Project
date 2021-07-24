# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 19
Sun = 0
Start = [1,1,1,1900]
# Day of the week, DD,MM,YYYY
while Start[3]<1901:
    Start[0]+=1
    if Start[0] == 8:
        Start[0]-=7
    Start[1]+=1
    if [1,3,5,7,8,10,12].count(Start[2]) == 1 and Start[1] == 32:
        Start[1]-=31
        Start[2]+=1
        if Start[0] == 7:
            Sun += 1   
        if Start[2] == 13:
            Start[2] -= 12
            Start[3] += 1
    if [9,4,6,11].count(Start[2]) == 1 and Start[1] == 31:
        Start[1]-=30
        Start[2]+=1   
        if Start[0] == 7:
            Sun += 1
    if Start[2] == 2 and Start[1] == 29:
        Start[1]-=28
        Start[2]+=1        
        if Start[0] == 7:
            Sun += 1        
print(Sun, 'Sundays in 1900.')
Sun = 0
while Start[3]<2001:
    Start[0]+=1
    if Start[0] == 8:
        Start[0]-=7
    Start[1]+=1
    if [1,3,5,7,8,10,12].count(Start[2]) == 1 and Start[1] == 32:
        Start[1]-=31
        Start[2]+=1
        if Start[0] == 7:
            Sun += 1   
        if Start[2] == 13:
            Start[2] -= 12
            Start[3] += 1
    if [9,4,6,11].count(Start[2]) == 1 and Start[1] == 31:
        Start[1]-=30
        Start[2]+=1   
        if Start[0] == 7:
            Sun += 1
    if Start[2] == 2 and Start[1] == 29:
        if Start[3]%4 !=0:
            Start[1]-=28
            Start[2]+=1        
            if Start[0] == 7:
                Sun += 1
        else:
            Start[1]-=29
            Start[2]+=1        
            if Start[0] == 6:
                Sun += 1            
print(Sun, 'Sundays in the 20th century.')
# # This code is inefficient, but it works. A better method is to take the months mod 7 and find how far along the week they progress the dates. It could even go one step further if you partician the years according to the pattern of starting day and leap year/non-leap year.