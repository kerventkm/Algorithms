from random import randrange
import re


n = 7
k = 5
S = [4, 8, 3, 9, 15, 11, 2]

def Select(S, k):
    a_i = S[randrange(len(S))]
    S_negative = []
    S_positive = []
    for a in S:
        if a < a_i:
            S_negative.append(a)
        elif a > a_i:
            S_positive.append(a)
    l = len(S_negative)
    if l == k - 1:
        return a_i
    elif l > k - 1:
        return Select(S_negative, k)
    else:
        return Select(S_positive, k - 1 - l)
    

print(Select(S, k)) 