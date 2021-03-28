# https://www.hackerrank.com/challenges/service-lane/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def serviceLane(width, cases):
    a = []
    for x in cases:
        a.append(min(width[x[0]:x[1]+1]))
    return a



print(serviceLane([2, 3, 1, 2, 3, 2, 3, 3],[[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]))