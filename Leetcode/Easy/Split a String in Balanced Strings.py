# https://leetcode.com/problems/split-a-string-in-balanced-strings/
# 1221
def balancedStringSplit(s):
    r, l, a = 0, 0, 0
    for x in s:
        if x == 'R':
            r += 1
        else:
            l += 1
        if l == r:
            r = 0
            l = 0
            a += 1
    return a


print(balancedStringSplit(s="RLRRRLLRLL"))
