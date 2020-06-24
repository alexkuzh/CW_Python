#https://www.codewars.com/kata/56bdd0aec5dc03d7780010a5/train/python
def next_higher(value):
    s = "{0:b}".format(value)
    s = s.zfill(len(s)+1)
    m = s.rfind('01')
    # res = s[0:m]+'10'+s[m+2:]
    z = sorted(list(s[m:]))
    res = s[:m]+'1'+ ''.join(z[:-1])
    print(s)
    print(res)
    # print("{0:b}".format(value<<1))
    print('0'+"{0:b}".format(360289361))
    return int(res,2)


print(next_higher(62))