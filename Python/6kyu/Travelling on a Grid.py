# https://www.codewars.com/kata/5845b080a87f768aaa00027c/train/python
import itertools as it


def travel_chessboard_1(s):
    x, y = int(s[6]) - int(s[1]), int(s[8]) - int(s[3])
    return len(set(it.permutations('0' * x + '1' * y, x + y)))


def travel_chessboard(s):
    x, y = int(s[6]) - int(s[1]), int(s[8]) - int(s[3])
    r = 0
    for k in range(2 ** (x + y), 4 ** (x + y)):
        if bin(k)[3:].count('0') == x and bin(k)[3:].count('1') == y and len(bin(k)[3:]) == x + y:
            r += 1
            print(bin(k)[3:])
    return r


def travel_chessboard_2(s):
    x, y = int(s[6]) - int(s[1]), int(s[8]) - int(s[3])
    r = 0
    for k in range(2 ** (x + y)):
        count = 0
        n = k
        while n:
            count += n & 1
            n >>= 1
        if count == y:
            r+=1
    return r


# print(travel_chessboard('(3 1)(7 8)'))
# print(travel_chessboard_1('(3 1)(7 8)'))
print(travel_chessboard_2('(3 1)(7 8)'))
# print(17 & 1)
# print(bin(19))
# print(19 >> 1)
