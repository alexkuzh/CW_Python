# https://www.codewars.com/kata/52840d2b27e9c932ff0016ae/train/python
def locate(seq, value):
    # your code here
    for s in seq:
        if s == value or type(s) is list and locate(s, value):
            return True
    return False



print(locate(['a','b',['c','d',['e']]],'c'))