# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 21:53:37 2021

@author: Cnoized
"""
#This is for problem 54

import pandas

file = pandas.read_csv('Problem54.csv', header=None)
# print(file)
data = []
file.values.tolist()
for n in file.values:
    # print(n)
    # print(str(n))
    n=str(n[0]).split(' ')
    # print(n)
    # n = [int(a) for a in n]
    data.append(n)
P1K = []
P2K = []
for n in data:
    P1K.append(n[0:5])
    P2K.append(n[5:10])
# print(P1K[0])
# print(P2K[0])
# print(P1K[-1])
# print(P2K[-1])

# # Imported data to each player.

# Let hand be H

H = ['AD', 'KD', '3D', 'JD', '8D']

if H[0][1] == H[1][1] == H[2][1] == H[3][1] == H[4][1]:
    # print('Flush')
    Flush = 0
else:
    Flush = 1
    # print('not flush')
# H = [ord(H[a][0]) for a in range(5)]
# print(H)
# i=0
Alphabet = ['A','K','Q','J','T','9','8','7','6','5','4','3','2','A']
Alpha = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
# set(H) == set(Alphabet[i:i+5])
Straight_P1K = []
Tuple_P1K = []
###### Going to come back to this. #######

def Hand(Hand):
    H = Hand
    Value = 0
    h = [Alpha[H[j][0]] for j in range(5)]
    h = sorted(h,reverse = True)
    # print(h)
    h = sorted(h,key=h.count,reverse = True)
    # print(h)
    for n in range(len(h)):
        Value += h[n]/(100**(n+1))
    # print(Value)
    V = [H[j][0] for j in range(5)]    
    if H[0][1] == H[1][1] == H[2][1] == H[3][1] == H[4][1]:
        # print('Flush')
        Value += 12
    
    Count_1 = max([h.count(i) for i in h])
    # print(Count_1)
    if Count_1 == 1:
        Value += 1
        # print('High card:',h[0])
    if Count_1 == 2:
        Value += 2
        # print('Pair')
        if h[2]==h[3]:
            Value += 1
            # print('Two Pair')
        
    if Count_1 == 3:
        Value += 4
        # print('Three of a Kind')
        if h[3]==h[4]:
            Value += 1
            # print('Full House')
    if Count_1 == 4:
        Value += 7
        # print('Four of a Kind')
    Straight = sum([(len(Alphabet)-i)*(set(V) == set(Alphabet[i:i+5])) for i in range(len(Alphabet)-4)])
    if Straight > 0:
        Value += 10
        # print('Straight')
    return Value
P1W = 0  
Tie = 0
P2W = 0
for n in range(0,1000):
    if Hand(P1K[n])>Hand(P2K[n]):
        P1W += 1
    elif Hand(P1K[n])==Hand(P2K[n]):
        Tie += 1
    else:
        P2W += 1
#     H = [a for a in P1K[n]]
#     Q = [a for a in P2K[n]]
#     # Four = Full = Two_Pair = Three = Pair = Flush = Straight = 0
#     h = [H[j][0] for j in range(5)]
#     V = [Alpha[H[j][0]] for j in range(5)]
#     print(V)
#     if H[0][1] == H[1][1] == H[2][1] == H[3][1] == H[4][1]:
#         # print('Flush')
#         Flush = 1
#     Count_1 = max(h,key=h.count())
#     # else:
#     #     if [h.count(j) for j in Alphabet[:-1]].count(4) != 0:
#     #         Four = [h.count(j) for j in Alphabet[:-1]].index(4)
#     #         # print('Four')
#     #     elif [h.count(j) for j in Alphabet[:-1]].count(3) != 0 and [h.count(j) for j in Alphabet[:-1]].count(2) != 0:
#     #         Full = [[h.count(j) for j in Alphabet[:-1]].index(3), [h.count(j) for j in Alphabet[:-1]].index(2)]
#     #         # print('Full')
#     #     elif [h.count(j) for j in Alphabet[:-1]].count(3) != 0:
#     #         Three = [[h.count(j) for j in Alphabet[:-1]].index(3)]
#     #         # print('Three')
#     #     elif [h.count(j) for j in Alphabet[:-1]].count(2) == 2:
#     #         Two_Pair = [1 if h.count(j)== 2 else 0 for j in Alphabet[:-1]]
#     #         # print('Two pair')
#     #     elif [h.count(j) for j in Alphabet[:-1]].count(2) == 1:
#     #         Pair = [h.count(j) for j in Alphabet[:-1]].index(2)
#     #     #     print('Pair')
#     #     # print('not flush')
#     Straight = sum([(len(Alphabet)-i)*(set(h) == set(Alphabet[i:i+5])) for i in range(len(Alphabet)-4)])
    
#     # Tuple_P1K = [Flush*Straight,Four,Full,Flush,Straight,Three,Two_Pair,Pair,h]
#     # Tuple_P2K = []
    
#     # Four = Full = Two_Pair = Three = Pair = Flush = Straight = 0
#     h = [Q[j][0] for j in range(5)]
#     # if Q[0][1] == Q[1][1] == Q[2][1] == Q[3][1] == Q[4][1] and sum([(len(Alphabet)-i)*(set(h) == set(Alphabet[i:i+5])) for i in range(len(Alphabet)-4)]) != 0:
#         # if 
#     if [h.count(j) for j in Alphabet[:-1]].count(4) != 0:
#         Four = [h.count(j) for j in Alphabet[:-1]].index(4)
#         # print('Four')
    
#         # print('Flush')
        
#     else:
#         if 1==1:
#             print(V)
#         elif [h.count(j) for j in Alphabet[:-1]].count(3) != 0 and [h.count(j) for j in Alphabet[:-1]].count(2) != 0:
#             Full = [[h.count(j) for j in Alphabet[:-1]].index(3), [h.count(j) for j in Alphabet[:-1]].index(2)]
#             # print('Full')
#         elif [h.count(j) for j in Alphabet[:-1]].count(3) != 0:
#             Three = [[h.count(j) for j in Alphabet[:-1]].index(3)]
#             # print('Three')
#         elif [h.count(j) for j in Alphabet[:-1]].count(2) == 2:
#             Two_Pair = [1 if h.count(j)== 2 else 0 for j in Alphabet[:-1]]
#             # print('Two pair')
#         elif [h.count(j) for j in Alphabet[:-1]].count(2) == 1:
#             Pair = [h.count(j) for j in Alphabet[:-1]].index(2)
#             # print('Pair')
#         # print('not flush')
#     Straight = sum([(len(Alphabet)-i)*(set(h) == set(Alphabet[i:i+5])) for i in range(len(Alphabet)-4)])
#         # print('Straight')
#     Tuple_P2K.append([[b if type(a) == list else a for b in a] for a in [Flush*Straight,Four,Full,Flush,Straight,Three,Two_Pair,Pair,h]])
# P1W = 0

# for a in range(0,1000):
#     for n in range(len(Tuple_P1K)-1):
#         print(Tuple_P1K[a])
#         if Tuple_P1K[a][n] > Tuple_P2K[a][n]:
#             P1W += 1
print('P1W:',P1W)
print('Ties:',Tie)
print('P2W:',P2W)
    # Tuple_P1K.append()
# print(Tuple_P1K)
# print(Straight_P1K)
# print('Alphabet', Alphabet)



# # for H in P1K:
# print([H[j][0] for j in range(5)])
# print(sum([(len(Alphabet)-i)*(set(['2','A','K','Q','J']) == set(Alphabet[i:i+5])) for i in range(len(Alphabet))]))
# # print(Straight_P1K)
# print('Alphabet', Alphabet)


# # Build hand reading.