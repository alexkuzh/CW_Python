# https://www.codewars.com/kata/beginner-series-number-3-sum-of-numbers/train/python
def get_sum(a,b):
    if a == b: return a
    acc = 0
    t = sorted([a,b])
    for i in range(t[0],t[1]+1):
        acc +=i
    return acc

print(get_sum(-1,2))
'''
ddd
'''