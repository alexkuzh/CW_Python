# https://www.codewars.com/kata/536950ffc8a5ca9982001371/train/python

def solution(r):
    # print(r)
    # if r[0] < 0:
    #     return 1
    i = 0
    p = 0
    while p <= len(r):
        p += 1
        #print(r[i])
        try:
            i += r[i]
        except:
            return p
        if i >= len(r) or i<0:
            return p
    return -1

print(solution([2, 1, -3, 5, 3, 8, 7, 0, -3, 3, 2]))
# 4