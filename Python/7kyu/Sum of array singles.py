# https://www.codewars.com/kata/59f11118a5e129e591000134/train/python
def repeats(arr):
    # a = 0
    # for x in set(arr):
    #     if arr.count(x) == 1:
    #         a += x
    return sum([x for x in arr if arr.count(x) == 1])


print(repeats([4, 5, 7, 5, 4, 8]))
