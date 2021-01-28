# https://leetcode.com/problems/reverse-integer/solution/
def reverse(x):
    n = int(str(abs(x))[::-1]) * (1 if x > 0 else -1)
    return n if n <= (2 ** 31) - 1 and n >= - (2 ** 31) else 0


print(reverse(12564))
