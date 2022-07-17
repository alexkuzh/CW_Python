# https://www.hackerrank.com/challenges/itertools-product/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
a = tuple(map(int,input().split(' ')))
b = tuple(map(int,input().split(' ')))
print(', '.join([str((x,y))for x in a for y in b]))
