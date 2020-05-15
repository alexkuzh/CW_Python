#   https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
def is_valid_walk(walk):
    #determine if walk is valid
    n = walk.count('n')
    s = walk.count('s')
    w = walk.count('w')
    e = walk.count('e')
    return n==s and w==e and len(walk) == 10

print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))