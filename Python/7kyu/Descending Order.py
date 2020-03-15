# https://www.codewars.com/kata/5467e4d82edf8bbf40000155
def descending_order(num):
    l = list(str(num))
    l.sort()
    s = ''
    for i in l:
        s = str(i) + s
    return int(s)