# https://leetcode.com/problems/reverse-string/
def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()
        n = s[::-1].copy()
        for i in range(len(n)):
            s[i] = n[i]

        return s


print(reverseString(['w','e','r']))