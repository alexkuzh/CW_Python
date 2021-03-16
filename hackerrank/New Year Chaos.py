# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''Complete the function minimumBribes in the editor below. It must print an integer representing
the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.
minimumBribes has the following parameter(s):
q: an array of integers'''

def minimumBribes(q):
    a = 0
    for i in range(len(q)-1,0,-1):
        if q[i] - (i + 1) > 2:
            return print("Too chaotic")
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                a +=1
    return print(a)

s = '5 1 2 3 7 8 6 4'
arr = list(map(int, s.rstrip().split()))

minimumBribes(arr)