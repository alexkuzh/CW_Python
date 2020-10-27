# https://www.codewars.com/kata/54acd76f7207c6a2880012bb
# не доделан
def decodeBitsAdvanced1(bits):
    flag = int(bits[0])
    s = 0
    c = 0
    res = ''
    for x in bits:
        if flag != int(x):
            if c > 0:
                if c <= 3:
                    res += '.'
                else:
                    res += '-'
            else:
                if s <= 3:
                    res += ''
                elif 3 < s <= 6:
                    res += ' '
                else:
                    res += '   '
            s = 0
            c = 0

        if int(x):
            c += 1
            flag = int(x)
        else:
            s += 1
            flag = int(x)

    return res.strip()


def decodeBitsAdvanced2(bits):
    a = sorted(list(set(bits.split('0'))))[1:]
    koef_0_short = (len(min(a)) + len(max(a))) / 3
    koef_0_long = koef_0_short * 2
    a = sorted(list(set(bits.split('1'))))[1:]
    koef_1 = (len(min(a)) + len(max(a))) / 2

    print(koef_0_short, koef_0_long, koef_1)
    one, zero = 0, 0

    res = ''
    for x in bits:
        if int(x):
            if zero:
                if zero >= koef_0 * 2:
                    res += '   '
                elif zero > koef_0:
                    res += ' '
                else:
                    res += ''
                zero = 0
                one += 1
            else:
                one += 1
        else:
            if one:
                if one >= koef_1:
                    res += '-'
                else:
                    res += '.'
                one = 0
                zero += 1
            zero += 1
    return res.strip()


def decodeBitsAdvanced(bits):
    if bits == '': return ''
    a0 = [x for x in bits.split('1') if x != '']
    a1 = [x for x in bits.split('0') if x != '']
    if int(bits[0]):
        a1, a0 = a0, a1
    # print(a0,a1)
    a = []
    i0, i1 = 0, 0
    for i in range(len(a0 + a1)):
        if i % 2:
            if a1:
                a.append(a1[i1])
                i1 += 1
        else:
            if a0:
                a.append(a0[i0])
                i0 += 1

    b = []
    spaces = [[1], [2], [6]]
    dots = [[1], [3]]
    for x in a:
        if int(x[0]):
            t = {}
            t['0'] = abs(len(x) - sum(dots[0]) / len(dots[0]))
            t['1'] = abs(len(x) - sum(dots[1]) / len(dots[1]))
            t = sorted(t.items(), key=lambda x: x[1])
            dots[int(t[0][0])].append(len(x))
            if t[0][0] == '0':
                b.append('.')
            else:
                b.append('-')
            print(dots)
        else:
            t = {}
            t['0'] = abs(len(x) - sum(spaces[0]) / len(spaces[0]))
            t['1'] = abs(len(x) - sum(spaces[1]) / len(spaces[1]))
            t['2'] = abs(len(x) - sum(spaces[2]) / len(spaces[2]))
            t = sorted(t.items(), key=lambda x: x[1])
            spaces[int(t[0][0])].append(len(x))
            # print(spaces)

            if t[0][0] == '0':
                b.append('')
            elif t[0][0] == '1':
                b.append(' ')
            else:
                b.append('   ')

    return ''.join(b).strip()


print(decodeBitsAdvanced('111000111'))

# print(decodeBitsAdvanced(
#     '0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000'))
# ···· · −·−−   ·−−− ··− −·· ·
