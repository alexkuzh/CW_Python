# https://www.codewars.com/kata/5254ca2719453dcc0b00027d
def perm(l):
    if not l:
        return [[]]
    res = []
    for e in l:
        temp = list(l[:])
        temp.remove(e)
        res.extend([[e] + r for r in perm(temp)])
    return res

def permutations(d):
    s = perm(d)
    f = []
    for x in s:
        f.append(''.join(x))
    f = list(set(f))
    f.sort()
    return f