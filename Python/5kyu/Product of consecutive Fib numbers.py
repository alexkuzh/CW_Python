# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python
#Вот как надо!!!
# def productFib(prod):
#     a, b = 0, 1
#     while prod > a * b:
#         a, b = b, a + b
#     return [a, b, prod == a * b]

import math


def findIndex(n):
    fibo = math.log(n) * 2.078087 + 1.672276
    # returning rounded off value of index
    return round(fibo)


def fibo(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def nearest_fib(n):
    logroot5 = math.log(5) / 2
    logphi = math.log((1 + 5 ** 0.5) / 2)
    if n == 0:
        return 0
    # Approximate by inverting the large term of Binet's formula
    y = int((math.log(n) + logroot5) / logphi)
    lo = fibo(y)
    hi = fibo(y + 1)
    return lo if n - lo < hi - n else hi


def productFib(prod):
    if prod == 0: return [0,1,True]
    i = findIndex(nearest_fib(prod))
    while i > 1:
        if fibo(i) * fibo(i - 1) > prod:
            i -= 1
        elif fibo(i) * fibo(i - 1) == prod:
            return [fibo(i - 1), fibo(i), True]
        else:
            return [fibo(i), fibo(i + 1), False]


print(productFib(74049690))

