# https://www.hackerrank.com/challenges/funny-string/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def funnyString(s):
    for i in range(len(s) // 2):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(s[len(s) - i - 2]) - ord(s[len(s) - i - 1])):
            return 'Not Funny'
    return 'Funny'

print(funnyString('asfd'))