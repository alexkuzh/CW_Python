# https://www.codewars.com/kata/5d16af632cf48200254a6244/train/python
def strongest_even(n, m):
    while m & m - 1 >= n:
        m &= m - 1
    return m


print(strongest_even(33, 40))