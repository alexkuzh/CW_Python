# https://www.codewars.com/kata/5e2733f0e7432a000fb5ecc4
def get_free_urinals(s):
    s = '10' + s + '01'
    k = 0
    p = False
    sum = 0
    for i in s:
        if i == '0':
            k += 1
            p = False
        else:
            if p:
                sum = -1
                break
            p = True
            if k >= 3:
                sum += (k - 3) // 2 + 1
            k = 0
    return sum