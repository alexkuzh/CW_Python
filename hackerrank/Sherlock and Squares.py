# https://www.hackerrank.com/challenges/sherlock-and-squares/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
import math


def squares(a, b):
    # i = 0
    # for x in range(math.ceil(a ** 0.5), int(b ** 0.5) + 1):
    #     i += 1
    # return i

    #или так

    return math.floor(b ** 0.5) - math.ceil(a**0.5) +1

print(squares(100, 1000))
