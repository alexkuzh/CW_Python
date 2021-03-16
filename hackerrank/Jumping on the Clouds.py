# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.
jumpingOnClouds has the following parameter(s):
c: an array of binary integers'''

def jumpingOnClouds(c):
    return len(''.join(map(str, c)).replace('00000','0000').replace('000','00').replace('1', '')) - 1

s = '0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0'
c = list(map(int, s.rstrip().split()))

print(jumpingOnClouds(c))
