# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

def next_bigger(n):
    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1
    a = n
    while True:
        a += 1
        if sorted(str(a)) == sorted(str(n)):
            return a

print(next_bigger(459853)) #459853  483559
# print(next_bigger(2017))



