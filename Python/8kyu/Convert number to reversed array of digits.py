# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
def digitize(n):
    return list(map(int,list(str(n))))[::-1]


print(digitize(13145))
