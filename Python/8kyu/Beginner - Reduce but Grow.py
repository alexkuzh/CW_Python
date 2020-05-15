# https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python
from operator import mul
from functools import reduce

def grow1(arr):
    return reduce(mul, arr)

def grow(arr):
    a = 1
    for x in arr:
        a *=x
    return a

print(grow1([1,2,3,4]))