# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def unique_in_order(iterable):
    a = ''
    s = []
    for i in iterable:
        if i != a:
            s.append(i)
            a = i
    return s

print(unique_in_order('AAAABBBCCDAABBB'))