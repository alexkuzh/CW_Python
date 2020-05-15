# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python
import math

def zeros(n):
    a = 0
    s = ''
    for i in range(1,int(n**0.5)):
        s += ' +n//'+str(5**i)
        a += n//(5**i)
    return (a,s)
d = 30

print(math.factorial(d))
print(zeros(d))
