# https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python
def divisors(n):
    i = 1
    a = []
    while i <= n :
        if n % i==0 :
            a.append(i)
        i = i + 1
    return (a[1:-1] if len(a)>2 else '{} is prime'.format(n))
print(divisors(4))