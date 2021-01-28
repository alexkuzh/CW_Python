#https://leetcode.com/problems/valid-anagram/solution/
def isAnagram(s,t):
    return sorted(s) == sorted(t)

print(isAnagram('asdf','sdfaa'))