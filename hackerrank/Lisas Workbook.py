# https://www.hackerrank.com/challenges/lisa-workbook/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def divide(n, k):
    a = []
    b = list(range(1, n + 1))
    for x in range(n // k + 1):
        if b:
            a.append(b[:k])
            del b[:k]
    return a


def workbook(n, k, arr):
    a = []
    i, r = 0, 0
    for x in arr:
        for y in divide(x, k):
            i += 1
            a.append(y)
            print(i, y)
            if i in y:
                r += 1
    return r


s = '3 8 15 11 14 1 9 2 24 31'
arr1 = list(map(int, s.rstrip().split()))
print(workbook(10, 5, arr1))
# print(divide(6,3))
