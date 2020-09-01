# https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python
from itertools import product as it


def hamming(n):
    l = list(range(30))
    ar = []
    for a, b, c in it(l, repeat=3):
        # print(a, b, c)
        if a<30 and b<20 and c<15:
            ar.append ((2 ** a) * (3 ** b) * (5 ** c))
        # print(a,b,c,s)
    return sorted(ar)[n-1]
    # return sorted([(2 ** a) * (3 ** b) * (5 ** c) for a, b, c in it(list(range(4)), repeat=3)])[n-1]


print(hamming(511))
