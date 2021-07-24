# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 22

import pandas
file = pandas.read_csv('Problem22.csv', header=None, keep_default_na=False, na_values=['_'])
# # Pandas wanted to interpret one of the values as NaN instead of 'NA', so I had to include the last settings in the line.
print(file)
print(file.values)
data = []
for a in file.values:
    Names = [n for n in a]
print(file.values)
print(Names)
# Names.sort()
i = 1
Value = 0
for n in range(len(Names)):
    print(Names[n])

    Names[n] = [ord(a)-64 for a in Names[n]]
    #ord(a)-64 works for my computer. I think keyboard layout is different for mine. Looked like -96 was the goto for others.
    print(Names[n])
Names.sort()
for n in Names:
    Value += sum(n)*i
    i += 1
print(Value)
# print(file)
# print(file.values)
# for n in file.values:
#     print(n)
#     print(str(n))
#     n=str(n[0]).split(' ')
#     print(n)
#     # n = [int(a) for a in n]
#     data.append(n)
