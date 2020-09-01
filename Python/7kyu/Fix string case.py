# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python
def solve(s):
    if len([x for x in s if x.islower()]) >= len(s)//2:
        return s.lower()
    else: return s.upper()

print(solve('Code'))