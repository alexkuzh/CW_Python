# https://www.hackerrank.com/challenges/word-order/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

n = int(input())
d = {}
for i in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
print(len(d))
print(*d.values())
