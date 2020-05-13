# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
def rgb(r, g, b):
    # your code here :)
    r1 = hex(r)[2:].upper().zfill(2) if r > 0 and r < 256 else '00' if r <= 0 else 'FF'
    g1 = hex(g)[2:].upper().zfill(2) if g > 0 and g < 256 else '00' if g <= 0 else 'FF'
    b1 = hex(b)[2:].upper().zfill(2) if b > 0 and b < 256 else '00' if b <= 0 else 'FF'
    return '{}{}{}'.format(r1,g1,b1)

print(rgb(258, 2, 3))
