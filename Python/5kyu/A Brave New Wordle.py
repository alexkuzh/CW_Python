# https://www.codewars.com/kata/62013b174c72240016600e60/train/python

def resolver(guess, solution):
    res = ['b']*5
    sl = list(solution)
    gs = list(guess)

    for i in range(5):
        if gs[i] == sl[i]:
            res[i] = 'g'
            sl[i] = ''
            gs[i] = '_'
    print(gs, sl, res)

    for i in range(5):
        if gs[i] in sl:
            res[i] = 'y'
            print(gs[i])
            sl.remove(gs[i])
    print(gs, sl, res)

    return ''.join(res)


# print(resolver('wooer', 'ivory'))
print(resolver('xxxxz', 'yyyyx')) #ybbbb
# print(resolver('reads', 'sales')) # byybg

