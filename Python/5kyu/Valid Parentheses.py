# https://www.codewars.com/kata/52774a314c2333f0a7000688
def valid_parentheses(string):
    a = 0
    for s in string:
        if s == '(': a += 1
        if s == ')': a -= 1
        if a < 0: return False
    return a == 0