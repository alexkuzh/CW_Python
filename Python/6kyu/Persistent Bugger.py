# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
def persistence(n):
# your code
    i = 0
    while n>9:
        m = 1
        for x in map(int,str(n)):
            m *= x
        n = m
        i += 1
    return i

print(persistence(999))