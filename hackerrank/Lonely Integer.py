#https://www.hackerrank.com/challenges/lonely-integer/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
def lonelyinteger(a):
    for x in set(a):
        if a.count(x) == 1:
            return x
    return 0


print(lonelyinteger([1,2,3,4,3,2,1]))