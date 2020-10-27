# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python
def clean_string(s):
    # your code here
    l = list(s)
    while '#' in l:
        if l.index('#') > 0:
            del l[l.index('#')-1]
        l.remove('#')
    return ''.join(l)

print(clean_string('abc#d##c'))