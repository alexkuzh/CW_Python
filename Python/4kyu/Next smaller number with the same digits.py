# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python
def next_smaller(n):
    s = list([int(x) for x in str(n)])
    if s == sorted(s):
        return -1
    minim = 9
    for i in range(len(s)-1,-1,-1):
        if s[i]>minim:
            break
        minim = s[i]

    print(f'minim={minim}, index={i}, element={s[i]}')
    arr2 = s[i:]
    m = min([x for x in s[i:] if x < s[i]], key=lambda x: abs(x - s[i]))
    arr2.remove(m)
    d = s[:i]
    d.append(m)
    d.extend(sorted(arr2,reverse=True))
    if d[0] == 0:
        return -1
    return int(''.join(map(str,d)))


print(next_smaller(1023456789))  #790
