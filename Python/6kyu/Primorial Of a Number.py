# https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124/train/python

def prime(i, primes):
    for pr in primes:
        if not (i == pr or i % pr):
            return False
    primes.add(i)
    return i


def historic(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1


def num_primorial(n):
    # your code here
    r = 1
    for x in historic(n):
        r = r*x
    return r


print(num_primorial(3))

print(historic(10))
