# https://www.codewars.com/kata/546d15cebed2e10334000ed9

import re


def solve_runes(runes):
    m = re.findall(r'[+-]?[\?\d]+', runes)
    if runes.find('*') > 0:
        m.append('*')
    elif runes.find('--') > 0:
        m.append('-')
    else:
        m.append('+')
    t = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - set([int(x) for x in runes if x.isdigit()])
    for x in sorted(t):
        s1 = m[0].replace('?', str(x))
        s2 = m[1].replace('?', str(x))
        r = m[2].replace('?', str(x))
        if len(r) > 1 and int(r) == 0: continue
        if m[3] == '-' and int(s1) - int(s2) == int(r): return x
        if m[3] == '+' and int(s1) + int(s2) == int(r): return x
        if m[3] == '*' and int(s1) * int(s2) == int(r): return x
    return -1
