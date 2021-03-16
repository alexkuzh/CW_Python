# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
'''Complete the repeatedString function in the editor below. It should return an integer representing the number
of occurrences of a in the prefix of length  in the infinitely repeating string.
repeatedString has the following parameter(s):
s: a string to repeat
n: the number of characters to consider'''

def repeatedString(s, n):
    return (n // len(s)) * s.count('a') + s[:n % len(s)].count('a')



print(repeatedString('aba',10))
