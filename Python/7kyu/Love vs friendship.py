# https://www.codewars.com/kata/59706036f6e5d1e22d000016/solutions/python
def words_to_marks(s):
    # Easy one
    return sum([ord(x)-96 for x in s])

