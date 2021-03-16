# https://www.codewars.com/kata/59377c53e66267c8f6000027/train/python
'''
The left side letters and their power:
 w - 4
 p - 3
 b - 2
 s - 1

The right side letters and their power:
 m - 4
 q - 3
 d - 2
 z - 1'''


def alphabet_war(fight):
    # your code here
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    s = sum([left.get(x, 0) - right.get(x, 0) for x in fight])
    if s > 0:
        return 'Left side wins!'
    elif s < 0:
        return 'Right side wins!'
    return 'Let\'s fight again!'


print(alphabet_war('gedpp'))
