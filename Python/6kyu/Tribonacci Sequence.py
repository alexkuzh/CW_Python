# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python
def tribonacci(signature, n):
    #   your code here
    if n == 0: return []
    if n == 1: return signature[:1]
    if n == 2: return signature[:2]
    i = 3
    a = signature
    while i < n:
        a.append(sum(a[-3:]))
        i += 1
    return a

print(tribonacci([1, 1, 1],10))