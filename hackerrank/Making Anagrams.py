# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
'''
Given two strings,  and , that may or may not be of the same length,
determine the minimum number of character deletions required to make
and  anagrams. Any characters can be deleted from either of the strings.

For example, if  and , we can delete  from string  and  from string
so that both remaining strings are  and  which are anagrams.
'''


def makeAnagram(a, b):
    l = 'abcdefghijklmnopqrstuvwxyz'
    r = 0
    for x in l:
        r += abs(a.count(x)-b.count(x))
    return r


print(makeAnagram('bacdcwqb', 'dcbacf'))
