# https://www.codewars.com/kata/5f3afc40b24f090028233490/train/python
def swap(s,n):
    # whatever magic that'll happen here
    sa = list(s)
    sb = len(sa)//len(str(bin(n)[2:]))*str(bin(n)[2:])+str(bin(n)[2:])
    sr = ''
    j = 0
    for i in range(len(sa)):
        if sa[i].isalpha():
            sr += sa[i].swapcase() if int(sb[j]) else sa[i]
            j += 1
        else:
            sr += sa[i]
    return sr

print(swap('asfsdFSsdf', 0))