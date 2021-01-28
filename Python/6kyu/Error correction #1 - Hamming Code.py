# https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e/train/python
def encode(string):
    return ''.join([''.join([s * 3 for s in f'{ord(x):b}'.zfill(8)]) for x in string])


def decode(bits):
    string = ''
    for i in range(0,len(bits)-2,3):
        if bits[i:i+3] in ('110','101','011','111'):
            string +='1'
        else:
            string +='0'
    s = ''
    for i in range(0,len(string)-7,8):
        s += chr(int(string[i:i+8],2))
    return s


print(encode('hey'))
print(decode('000111111000111000000000000111111000000111000111000111111111111000000111'))
