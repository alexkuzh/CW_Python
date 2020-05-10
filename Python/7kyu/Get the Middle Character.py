# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
def get_middle(s):
    #your code here
    return s[len(s)//2-1: len(s)//2+1]


print(get_middle('asdfsdf'))