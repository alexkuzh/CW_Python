# https://www.codewars.com/kata/5626b561280a42ecc50000d1
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    l = []
    for x in range(a,b+1):
        p = 0
        for s in range(0, len(str(x))):
            p += int(str(x)[s])**(s+1)
        if x == p : l.append(x)
    return l