# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
def duplicate_encode(word):
    s = ''
    for x in word.lower():
        if word.lower().count(x) == 1:
            s += '('
        else:
            s += ')'
    return s