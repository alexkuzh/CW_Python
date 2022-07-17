# https://www.codewars.com/kata/5547cc7dcad755e480000004/train/python

def remov_nb(n):
    # your code
    for y in range(1, n + 1):
        x = (n * (1 + n) / 2 + 1) / (y + 1) - 1
        if x.is_integer() and x<n:
            return [(int(x), y), (y, int(x))]
    return []


print(remov_nb(1000003))
# n = 213
# y = 146
# x * y = n(1+n)/2 - x - y
# x + y + x*y = n(1+n)/2
# x+ y(x+1) = n(1+n)/2 +1
# (x+1)(y+1) = n(1+n)/2 +1
# x = (n * (1 + n) / 2 + 1) / (y + 1) - 1
# print(x.is_integer())
