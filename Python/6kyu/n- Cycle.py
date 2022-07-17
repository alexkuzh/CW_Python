# https://www.codewars.com/kata/5a057ec846d843c81a0000ad/train/python

l = ['a','b','c']
for x in l:
    print(x)
    if x == 'b':
        break
for x in l:
    if x == 'b':
        break
    print(x)


