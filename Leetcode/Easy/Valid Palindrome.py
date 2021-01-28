#https://leetcode.com/problems/valid-palindrome/
import re
def isPalindrome(s):
    a = ''.join(re.findall("[a-zA-Z0-9]+", s)).lower()
    return a == a[::-1]

# print(isPalindrome('A man, a plan, a canal: Panama'))
print(isPalindrome('ab_a'))