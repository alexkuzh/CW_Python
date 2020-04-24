# https://www.codewars.com/kata/59eb1e4a0863c7ff7e000008/train/python
import  itertools



def l(p):
    a = []
    for i in p:
        if len(i) == 2:
            a.append(i)
    return a

def solve(s,ops):
    #"tft","^&"
    a = ''
    for i in range(0, len(s) -1):
        a = a + s[i] + ops[i]
    a = a + s[-1]
    #print(en)
    p = []
    for n in range(2,len(s)):
        c = itertools.combinations(range(1,len(s)+1),n)
        for i in c:
            print(i)
            p.append(i)
    print(l(p))
    return a



print(solve("123456","*****"))

