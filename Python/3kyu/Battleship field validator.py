# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
def inter(st):
    s = [0, 0, 0]
    i = 0
    for x in st:
        if x == '1':
            i += 1
        else:
            if i == 2: s[0] += 1
            if i == 3: s[1] += 1
            if i == 4: s[2] += 1
            i = 0
    return s

def validate_battlefield(field):
    if sum(sum(x) for x in field) != 20: return False
    s1 = ''
    s2 = ''
    for row in field:
        s1 += '0' + ''.join([str(x) for x in row]) + '0'
    for row in zip(*field):
        s2 += '0' + ''.join([str(x) for x in row]) + '0'
    if sum(inter(s1)) + sum(inter(s2)) != 6:
        return False
    for n in range(0, 9):
        for i in range(0, 9):
            if field[n][i] == 1 and field[n + 1][i + 1] == 1: return False
        for i in range(1, 10):
            if field[n][i] == 1 and field[n + 1][i - 1] == 1: return False
    return True