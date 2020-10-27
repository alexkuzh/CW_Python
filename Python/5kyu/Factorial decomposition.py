# https://www.codewars.com/kata/5a045fee46d843effa000070/train/python
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def decomp1(n):
    a = [x + 1 for x in range(n)][1:]
    f = True

    while f:
        for y in a:
            f = False
            for x in a:
                if x % y == 0 and x > y:
                    a.insert(0,y)
                    a.append(x // y)
                    a.remove(x)
                    f = True
    s = sorted(set(a))
    r = []
    # return s
    for x in s:
        r.append(str(x)+ ('^'+str(a.count(x)) if a.count(x)>1 else '') )
    return ' * '.join(r)


def decomp(n):
    a = [x + 1 for x in range(n)][1:]
    b = []
    for x in a:
        b += prime_factors(x)

    s = sorted(set(b))
    r = []
    for x in s:
        r.append(str(x)+ ('^'+str(b.count(x)) if b.count(x)>1 else '') )
    return ' * '.join(r)

# print(prime_factors(3990))


print(decomp(4000))


'''
2*3*4*5*6*7*8*9*10*11*12
7*11
2*2*2*2*2*2*2*2*2*2
3*3*3*3*3
5*5
'''
