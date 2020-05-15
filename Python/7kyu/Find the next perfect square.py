# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
import math


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return (math.sqrt(sq) + 1) ** 2 if math.sqrt(sq).is_integer() else -1
