# https://www.codewars.com/kata/56c30ad8585d9ab99b000c54/train/python
def swap(a,b):
    res = ''
    k,l = a.lower(),b.lower()
    for i in range(len(a)):
        if l.count(k[i]) % 2 == 1:
            res += a[i].swapcase()
        else: res += a[i]
    return res

def work_on_strings(a,b):
    return swap(a, b) + swap(b, a)

# abcDEfg DEFGg
print(work_on_strings("abcdeFg", "defgG"))