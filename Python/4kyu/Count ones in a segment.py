# https://www.codewars.com/kata/596d34df24a04ee1e3000a25/train/python

def count1(n):
    d = len(bin(n)[2:])
    return (int('1' * d, 2) + 1) // 2 * d


def countOnes(left, right):
    # Your code here!
    f = len(bin(right)[2:])
    s = []
    for x in range(left, right + 1):
        print(bin(x)[2:].zfill(f))
        s += [int(m) for m in bin(x)[2:]]
    # print(sum(s))
    return sum(s)


r = 14 #37
print(f'all={countOnes(0, r)}')
s = 0
while r > 1:
    print(f'r= {r}')
    g = int('1'+'0'*(len(bin(r)[2:])-1),2)-1
    print(f'g={g}')
    s += count1(g)
    print(f's={s}')
    r -=g




# for n in range(1,64):
#     print(countOnes(1,n))
