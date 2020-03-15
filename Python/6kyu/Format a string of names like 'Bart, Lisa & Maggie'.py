# https://www.codewars.com/kata/53368a47e38700bd8300030d
def namelist(d):
    if d == []: return ''
    l = [x.get('name') for x in d]
    if len(l) == 1: return l[0]
    return ', '.join(l[:-1]) + ' & ' + l[-1]