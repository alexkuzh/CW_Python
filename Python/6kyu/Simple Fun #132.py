# https://www.codewars.com/kata/58a6568827f9546931000027/train/python
def number_of_carries(a, b):
    # coding and coding..
    p = 0
    r = 0
    while a > 0 or b > 0:
        a1 = a % 10
        b1 = b % 10
        s = p + a1 + b1
        if s >= 10:
            r += 1
        p = s >= 10
        a //= 10
        b //= 10
    return r


print(number_of_carries(544, 3456))
