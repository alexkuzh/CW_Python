# https://www.codewars.com/kata/552c028c030765286c00007d/train/python
def iq_test(numbers):
    # your code here
    s = [[], []]
    a = numbers.split(' ')
    for i in range(0, len(a)):
        s[0].append(i) if int(a[i]) % 2 == 0 else s[1].append(i)
    print(min(s[0], s[1], key=len)[0] + 1)
    return min(s[0], s[1], key=len)[0] + 1

print(iq_test('2 4 7 8 10'))
