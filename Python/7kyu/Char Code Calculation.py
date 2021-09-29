# https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/javascript
def calc(x):
    # your code here
    return ''.join([str(ord(ch)) for ch in x]).count('7')*6


print(calc('ifkhchlhfd'))