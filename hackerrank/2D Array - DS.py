# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.'''

def hourglassSum(arr):
    a = -70
    for i in range(4):
        for j in range(4):
            b = arr[i][j] + arr[i][j+1]+arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1]+arr[i+2][j+2]
            if a < b: a = b
    return a


arr = []
s = '-9 -9 -9  1 1 1 0 -9  0  4 3 2 -9 -9 -9  1 2 3 0  0  8  6 6 0 0  0  0 -2 0 0 0  0 1 2 4 0'
a = list(map(int, s.rstrip().split()))
print(a)
for i in range(6):
    arr.append(a[i*6:i*6+6])
print(arr)

print(hourglassSum(arr))