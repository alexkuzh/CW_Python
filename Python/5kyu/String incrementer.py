# https://www.codewars.com/kata/54a91a4883a7de5d7800009c
def increment_string(s):
    a = ''
    for i in range(len(s)-1, -1, -1):
        if s[i].isdigit():
            m = i
            a = s[i] + a
        else:
            break
    if a == '':
        return s + '1'
    else:
        return s[0:m] + str(int(a)+1).zfill(len(a))
    