# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
def longest_consec(strarr, k):
    # your code
    if k <= 0 or len(strarr)==0 or k>len(strarr): return ''
    l = ''
    for i in range(0, len(strarr) - k + 1):
        s = ''.join(strarr[i: i+k])
        if len(s)>len(l):
            l = s
    return l


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"],2))