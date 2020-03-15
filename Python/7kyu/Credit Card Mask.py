# https://www.codewars.com/kata/5412509bd436bd33920011bc
# return masked string
def maskify(cc):
    s = ''
    for x in range(0, len(cc) - 4): s += "#"
    if len(cc) > 4:
        for x in cc[len(cc) - 4: len(cc)]: s += str(x)
    else:
        s = str(cc)
    return s
