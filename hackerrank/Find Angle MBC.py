# https://www.hackerrank.com/challenges/find-angle/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
import math


def angle(a,b):
    return round(math.degrees(math.atan(a/b)))


a,b = int(input()),int(input())
print(f'{angle(a,b)}{chr(176)}')