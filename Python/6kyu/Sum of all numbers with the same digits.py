# https://www.codewars.com/kata/5eb9a92898f59000184c8e34/train/python
from itertools import permutations
import math
def sum_arrangements(num):
#your code here
    s = list(map(int, list(str(num))))
    k = sum(s)
    m = len(s)
    a = math.factorial(m)//m
    n = a*k*(10**m-1)//9
    return n

print(sum_arrangements(123))
# print(len([x for x in permutations([1,2,3,4])]))
# print([x for x in permutations([1,2,3,4])])