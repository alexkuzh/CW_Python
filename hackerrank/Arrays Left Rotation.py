# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen
'''Complete the function rotLeft in the editor below. It should return the resulting array of integers.
rotLeft has the following parameter(s):
An array of integers .
An integer , the number of rotations.'''

def rotLeft(a, d):
    for i in range(d):
        a.append(a.pop(0))
        print(a)
    return a

#s = '41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51'
s = '1 2 3 4 5'
n = 4

arr = list(map(int, s.rstrip().split()))

print(rotLeft(arr,n))