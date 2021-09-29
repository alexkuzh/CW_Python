# https://www.codewars.com/kata/53a1eac7e0afd3ad3300008b/train/python
def f(n):
    if n == 0:
        return 1
    while n>0:
        return n - m(f(n-1))

def m(n):
    if n == 0:
        return 0
    while n>0:
        return n - f(m(n-1))

print(f(10))