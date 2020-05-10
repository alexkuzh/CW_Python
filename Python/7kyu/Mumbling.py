# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
def accum(s):
    # your code
    res = ''
    for x in range(0,len(s)):
        res += (s[x]*(x+1)).title()+'-'
    return res[:-1]


print(accum('abcd'))