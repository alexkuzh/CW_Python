# https://www.codewars.com/kata/5f3142b3a28d9b002ef58f5e/train/python
def word_pattern(word):
    a, res = [], []
    for x in word.lower():
        if x not in a:
            a.append(x)
    for x in word.lower():
        res.append(str(a.index(x)))
    return '.'.join(res)


print(word_pattern('hello'))
