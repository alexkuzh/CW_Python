# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
def digital_root(n):
# ...
    a = list(map(int,str(n)))
    while len(a)>1:
        k = sum(a)
        a = list(map(int,str(k)))
    return a[0]

print(digital_root(4))