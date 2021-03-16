# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
'''For example, there are  socks with colors .
There is one pair of color  and one of color .
There are three odd socks left, one of each color. The number of pairs is .'''
# n  9
# ar 10 20 20 10 10 30 50 10 20

def sockMerchant(n, ar):
    ar = sorted(ar)
    a = 0
    while len(ar) > 1:
        if ar[0] == ar[1] :
            a += 1
            del ar[:2]
        else:
            del ar[0]
    return a

print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))