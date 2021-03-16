# https://www.hackerrank.com/challenges/find-digits/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def findDigits(n):
    return len([x for x in str(n) if x != '0' and n % int(x) == 0])


print(findDigits(123456789))
