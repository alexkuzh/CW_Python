# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python
def scramble(s1, s2):
# your code here
    d1 = {}
    d2 = {}
    for x in set(s1):
        d1[x]=s1.count(x)
    for x in set(s2):
        d2[x]=s2.count(x)
    for x in d2:
        try:
            if d2[x]>d1[x]: return False
        except:
            return False
    return True


print(scramble('katas', 'steak'))