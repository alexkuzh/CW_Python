# https://www.codewars.com/kata/62c93765cef6f10030dfa92b/train/python

def solution(start, finish):
    d = finish - start
    s = d //3 + d%3
    return s


print(solution(1,6))