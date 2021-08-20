# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 59

import pandas
file = pandas.read_csv('Problem59.csv', header=None)
print(file)
data = []
file.values.tolist()
for n in file.values:
    print(n)
    print(str(n))
#     n=str(n[0]).split(' ')
#     print(n)
#     n = [int(a) for a in n]
#     data.append(n)
# print(data)
# n = [int(a) for a in file.values]
# print(n)

#looking for 116 104 101
Space1 = []
Space2 = []
Space3 = []
for a in range(len(n)-6):
    if n[a] == n[a+6]:
        if a%3 == 0:
            Space1.append(a)
        elif a%3 == 1:
            Space2.append(a)
        else:
            Space3.append(a)
m_max = 0
for i in range(1,200):
    M = [ord('a') == a^i for a in Space1]
    m = sum(M)
    if m>m_max:
        m_max = m
        I = i
        print(i,m)
        
input()
THE=[116,104,101]
print(n)
print(THE)
p=0
Cypher = []
Can = []
MaxValid = len(n)
L = [a for a in n]
print(file.values)
for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            for n in file.values:
                n
            p=0
            while p<len(n):
                if p%3 == 0:
                    n[p]=n[p]^i
                elif p%3 == 1:
                    n[p]=n[p]^j
                elif p%3 == 2:
                    n[p]=n[p]^k
                p+=1
            # print(n[:10])
            TotalValid = 0
            for a in range(1,len(n)-3):
                if n[a] not in range(97,123) and n[a] not in range(65,92) and n[a] != 32 and n[a] != 44 and n[a] != 46 and n[a] not in range(49,58):
                    TotalValid+=1
                # if n[a]==ord('t') and n[a+1]==ord('h') and n[a+2]==ord('e'):
                #     # print(a,i,j,k)
                #     Cypher.append([a,i,j,k])
                #     TotalValid+=1
                #     print(chr(n[a+3]))
            if TotalValid <= MaxValid:
                MaxValid = TotalValid
                Can = [MaxValid,i,j,k]
                print(Can)
                # print([chr(n[a]) for a in n])
                # print(Can)
print(file.values)
print('Can = ', Can)
i=Can[1]
j=Can[2]
k=Can[3]
p=0
print([chr(a) for a in range(97,123)])
for n in file.values:
    print(n)
while p<len(n):
    if p%3 == 0:
        n[p]=n[p]^i
    elif p%3 == 1:
        n[p]=n[p]^j
    else:
        n[p]=n[p]^k
    p+=1
print([chr(n[a]) for a in n])

# Never got this program to work, but I was able to get the first two variables from looking at accuracy to normal words and phrases. Then performed troubleshooting on the final value of the key.