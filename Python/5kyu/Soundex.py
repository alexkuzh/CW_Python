# https://www.codewars.com/kata/587319230e9cf305bb000098/train/python

from itertools import groupby


def encode(name):
    name = name.upper()
    First_letter = name[0]
    name = name.replace('H', '').replace('W', '')
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    soundex_code = '7'
    for i in range(len(name)):
        code = mapping.get(name[i], '7')
        print(name[i], code)
        if code != soundex_code[-1]:
            soundex_code += code
    g = [k for k, g in groupby(soundex_code) if k != '7']
    # print(g)
    try:
        if mapping.get(First_letter, '7') == g[0]:
            soundex_code = ''.join(g[1:])
        else:
            soundex_code = ''.join(g)
    except:
        soundex_code = ''
    soundex_code = First_letter + soundex_code + '000'

    return soundex_code[:4]


def soundex(name):
    words = name.split(' ')
    print(words)
    l = []
    for word in words:
        l.append(encode(word))
    print(l)
    return " ".join(l)


# print(soundex("Sarah Connor"))
# print(encode('Pfister'))

name = "Washington"
code = soundex(name)
print(code)  # Output: W252
