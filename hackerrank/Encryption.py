# https://www.hackerrank.com/challenges/encryption/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
import math

def encryption(s):
    a = []
    o = ''
    r = int(len(s) ** 0.5)
    c = r + 1
    r = c if c*r<len(s) else r
    c = c-1 if r**2==len(s) else c
    print(len(s), r,c)
    for row in range(r):
        a.append(list(s[row * c:row * c + c]))
    print(a)
    for y in range(c):
        for x in a:
            try:
                o += x.pop(0)
            except:
                pass
        o += ' '
    return o.strip()

def encryption1(s):
    c = math.ceil(math.sqrt(len(s)))
    p = ' '.join(map(lambda x: s[x::c], range(c)))
    print(s[3::c])
    return p

print(encryption1('iffactsdontfittotheorychangethefacts'))
