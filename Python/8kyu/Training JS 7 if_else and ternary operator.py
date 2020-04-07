# https://www.codewars.com/kata/training-js-number-7-if-dot-else-and-ternary-operator/train/python
def sale_hotdogs(n):
    return n * 100 if n < 5 else n * 95 if  n>=5 and n <10 else n * 90

print(sale_hotdogs(9))