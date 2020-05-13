# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
def array_diff(a, b):
#your code here
    r = []
    for x in a:
        if x not in set(b): r.append(x)
    return r
 #   return [x for x in a if x not in b]

print(array_diff([1,2,2,2,3],[2]))