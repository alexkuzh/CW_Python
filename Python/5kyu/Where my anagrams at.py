# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python
def anagrams(word, words):
#your code here
    w = sorted(word)
    a = []
    for x in words:
        m = sorted(x)
        if w == m: a.append(x)
    return a

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))