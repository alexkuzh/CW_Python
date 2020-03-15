# https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0
import math

def who_is_next(names, r):
    return names[(r + len(names) - 1 - (2 ** math.floor(math.log2((r + len(names) - 1) / len(names)))) * len(names)) // 2 ** math.floor(
        math.log2((r + len(names) - 1) / len(names)))]