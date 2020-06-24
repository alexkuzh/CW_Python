# https://www.codewars.com/kata/5848565e273af816fb000449/train/python
def encrypt_this(text):
    arr = text.split(' ')
    s = []
    if not text: return ''
    for x in arr:
        if len(x) > 2:
            s.append(str(ord(x[0])) + x[-1] + x[2:-1] + x[1])
        elif len(x) == 2:
            s.append(str(ord(x[0]))+x[1])
        else:
            s.append(str(ord(x[0])))
    return ' '.join(s)



print(encrypt_this("A wise old owl lived in an oak"))