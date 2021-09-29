# https://www.hackerrank.com/challenges/kaprekar-numbers/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def kaprekarf(x):
    st_y = str(x**2)
    st_y = '0'+st_y if len(st_y)%2 else st_y
    # print(st_y)
    return int(st_y[:len(st_y) // 2]) + int(st_y[len(st_y) // 2:])


def kaprekarNumbers(p, q):
    a = []
    for x in range(p, q + 1):
        if x == kaprekarf(x):
            a.append(str(x))
    print(' '.join(a) if a else 'INVALID RANGE')

# print(kaprekarf(9))
kaprekarNumbers(1, 700)
