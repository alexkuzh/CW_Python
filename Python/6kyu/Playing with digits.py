# https://www.codewars.com/kata/5552101f47fc5178b1000050/python
def dig_pow(n, p):
    # your code
    s = str(n)
    a = 0
    for i in s:
        a += pow(int(i), p)
        p +=1
    k = a / n
    if k.is_integer(): return k
    return -1

print(dig_pow(46288, 3))