# https://www.hackerrank.com/challenges/chocolate-feast/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def chocolateFeast(n, c, m):
    r, w = 0, n // c
    r += w
    while w >= m:
        r += w // m
        w = w // m + w % m
    return r


print(chocolateFeast(10, 2, 5))
