# https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python
def longest_repetition(chars):
    if not chars: return ('',0)
    a = []
    c = '!'
    w = ''
    for x in chars:
        if x != c:
            c = x
            a.append(w)
            w = x
        else:
            w += x
    a.append(w)
    l = 0
    w = ''
    for x in a:
        if len(x) > l:
            l = len(x)
            w = x

    return (w[0], l)


print(longest_repetition("aabb"))
