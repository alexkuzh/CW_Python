# https://www.codewars.com/kata/56eb16655250549e4b0013f4/train/python
import calendar
import datetime


def most_frequent_days(year):
    s1 = set(range(datetime.date(year, 1, 1).weekday(), 7))
    s2 = set(range((datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)).weekday() + 1))
    if len(s1)<4 and len(s2)<4:
        l = list(s1 | s2)
    else:
        l = list(s1 & s2)
    a = []
    for x in l:
        a.append(calendar.day_name[x])
    return a


print(most_frequent_days(1984))
