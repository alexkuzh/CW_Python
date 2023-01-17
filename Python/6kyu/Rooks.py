# https://www.codewars.com/kata/5bc2c8e230031558900000b5/train/python
import math

def rooks(n, k):
    return math.comb(n, k) * math.perm(n, k)



print(rooks(4,2))

'''
0 1 2 3
0 1 2 3
0 1 2 3
0 1 2 3
'''