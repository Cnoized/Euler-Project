# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 85

Sigma_List = [0]
Count = 1
Number = 0
answer = 0
while answer < 2000000:
    answer += Count
    Sigma_List.append(answer)
    Count += 1
Max_Rectangles = 0
for x_axis in Sigma_List:
    for y_axis in Sigma_List:
        Rectangles = x_axis*y_axis
        if Rectangles<2000000 and Rectangles>Max_Rectangles:
            Max_Rectangles = Rectangles
            Max_Dimensions = [Sigma_List.index(x_axis),Sigma_List.index(y_axis)]
            print(Max_Dimensions,'and',2000000-Max_Rectangles)
            