# https://www.codewars.com/kata/54acd76f7207c6a2880012bb
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


def decodeBitsAdvanced(bits):
    a = sorted(list(set(bits.split('0'))))[1:]
    koef_0_short = (len(min(a)) + len(max(a))) / 3
    koef_0_long = koef_0_short * 2
    a = sorted(list(set(bits.split('1'))))[1:]
    koef_1 = (len(min(a)) + len(max(a))) / 2

    print(koef_0_short,koef_0_long, koef_1)
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
                one +=1
            else:
                one += 1
        else:
            if one:
                if one >= koef_1:
                    res += '-'
                else:
                    res += '.'
                one = 0
                zero +=1
            zero += 1
    return res.strip()


print(decodeBitsAdvanced(
    '0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000'))
