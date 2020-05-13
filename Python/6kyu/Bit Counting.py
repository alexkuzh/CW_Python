# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
def countBits(n):
    return bin(n)[2:].count('1')

print(countBits(1234))