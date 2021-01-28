# https://leetcode.com/problems/first-unique-character-in-a-string/
def firstUniqChar(s):
    for x in s:
        if s.count(x)==1:
            return s.index(x)
    return 0

print(firstUniqChar('asddsqada'))
