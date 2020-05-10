# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
def getCount(inputStr):
    return len(list(x for x in inputStr if x in ('a','i','e','u','o')))

print(getCount('asdsaerwdgfgsa'))