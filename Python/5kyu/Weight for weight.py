# https://www.codewars.com/kata/55c6126177c9441a570000cc
def order_weight(s):
    l = s.split(' ')
    a = []
    for i in l:
        a.append([i, str(sum([int(x) for y, x in enumerate(i, 1)])).zfill(len(max(l, key=len))) + i])
    a.sort(key=lambda e: e[1])
    return ' '.join([x for x,y in a])
