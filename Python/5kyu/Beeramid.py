# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/python
def beeramid(bonus, price):
    # your code
    if bonus<0:
        return 0
    k = bonus // price
    i = 1
    while True:
        k -= i ** 2
        if k < (i+1) ** 2:
            return i
        i += 1

print(beeramid(9, 2))
print(beeramid(9, 2))
print(beeramid(1500, 2))