# https://leetcode.com/problems/zigzag-conversion/
def convert(s, numRows):
    a = []
    if numRows == 1: return s
    while len(s):
        if len(a)%2 == 0:
            a.append(s[:numRows])
            s = s[numRows:]
        else:
            a.append(''.join(list(reversed(' '+s[:numRows-2]+' '))))
            s = s[numRows-2:]
    r = ''
    for i in range(numRows):
        for x in a:
            if i < len(x):
                r += x[i]
    return r.replace(' ','')

print(convert('ABCDE',4))