# https://www.codewars.com/kata/573182c405d14db0da00064e/train/python
def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def is_k_prime(k, num):
    while k > 0:
        f = False
        for l in range(2, num // 2):
            if is_prime(l):
                if num % l == 0:
                    num //= l
                    k -= 1
                    f = True
                if k < 0:
                    return False
                if is_prime(num) and k == 1:
                    return True
            if f:
                break
    return False


def consec_kprimes1(k, arr):
    m = 0
    dd = []
    p = False
    for x in arr:
        # dd.append(is_k_prime(k, x))
        t = is_k_prime(k, x)
        m += p * t
        p = t
    # print(dd)
    return m


def primes(n):
    primefac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primefac.append(d)
            n //= d
        d += 1
    if n > 1:
        primefac.append(n)
    return len(primefac)


def consec_kprimes(k, arr):
    return sum(primes(arr[i]) == primes(arr[i + 1]) == k for i in range(len(arr) - 1))


print(consec_kprimes(3, [10158, 10182, 10184, 10172, 10179, 10168, 10156, 10165, 10155, 10161, 10178, 10170]))
# print(consec_kprimes(2, [10110, 10102, 10097, 10113, 10123, 10109, 10118, 10119, 10117, 10115, 10101, 10121, 10122]))
# print(consec_kprimes(2, [10123, 10122, 10132, 10129, 10145, 10148, 10147, 10135, 10146, 10134]))
# print(consec_kprimes(6, [10176, 10164]))
# print(consec_kprimes(1, [10182, 10191, 10163, 10172, 10178, 10190, 10177, 10186, 10169, 10161, 10165, 10181]))
# print(is_k_prime(3,10184))
