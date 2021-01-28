# https://leetcode.com/problems/string-to-integer-atoi/solution/
def myAtoi(s):
    num = ""
    for l in s.strip():
        if l.isdigit() or (l in "+-" and not num) :
            num+=l
        else:
            break
    try:
        num = int(num)
    except:
        return 0
    return min(2**31-1, max(-2**31, int(num)))

print(myAtoi("  -0012a-42"))
