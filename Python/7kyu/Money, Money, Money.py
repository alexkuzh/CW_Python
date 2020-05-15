# https://www.codewars.com/kata/563f037412e5ada593000114/train/python
def calculate_years(p, i, t, d):
    y = 0
    while p < d:
        p += p * i * (1 - t)
        y += 1
    return y
