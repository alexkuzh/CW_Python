# https://www.hackerrank.com/challenges/utopian-tree/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def utopianTree(n):
    a = 0
    for n in range(n+1):
        if n%2:
            a*=2
        else:
            a+=1
    return a

print(utopianTree(5))