# https://www.hackerrank.com/challenges/minimum-distances/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
def minimumDistances(a):
    m = len(a)
    for i in range(len(a)):
        try:
            ix = a[i+1:].index(a[i])
        except:
            ix = len(a)
        if ix<m:
            m = ix+1
    return m if m<len(a) else -1

print(minimumDistances([7, 1, 3, 4, 2, 71]))