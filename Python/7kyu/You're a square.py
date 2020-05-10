# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
import math
def is_square(n):

    return int(math.sqrt(n))**2 == n if n>=0 else False

print(is_square(-1))