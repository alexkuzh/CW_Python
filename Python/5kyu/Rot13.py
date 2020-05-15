# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
def rot13(message):
    s = ''
    for x in message:
        if x.isalpha():
            if x.islower():
                s += chr((ord(x)-97+13)%26+97)
            else:
                s += chr((ord(x)-65+13)%26+65)
        else:
            s += x
    return s

print(chr((ord('t')-65+13)%26+65))
print(rot13('test'))