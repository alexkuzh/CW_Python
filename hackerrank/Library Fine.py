# https://www.hackerrank.com/challenges/library-fine/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 < y2:
        return 0
    if m1 > m2:
        return 500 * (m1 - m2)
    elif m1 < m2:
        return 0
    if d1 > d2:
        return 15 * (d1 - d2)
    return 0

print(libraryFine(2,7,1014,1,1,1015))