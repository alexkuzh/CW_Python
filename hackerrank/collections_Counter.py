# https://www.hackerrank.com/challenges/collections-counter/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
"""
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
"""
n = int(input())
l = list(map(int,input().split(' ')))
cust = int(input())
s = 0
for x in range(cust):
    d = list(map(int,input().split(' ')))
    # print(d)
    # print(l,s)
    try:
        l.remove(d[0])
        s+=d[1]
    except Exception:
        pass
print(s)
