# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
'''Function Description
Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.
countingValleys has the following parameter(s):
n: the number of steps Gary takes
s: a string describing his path'''
#8
#UDDDUDUU
def countingValleys(n, s):
    lev = 0
    valley = 0
    for x in s:
        l1 = lev
        lev += 1 if x == 'U' else -1
        if l1 == 0 and lev < 0 : valley += 1
    return valley

print(countingValleys(10,'UDUUUDUDDD'))