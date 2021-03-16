# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen
'''Complete the function minimumSwaps in the editor below. It must return an integer representing
the minimum number of swaps to sort the array.
minimumSwaps has the following parameter(s):
arr: an unordered array of integers'''

def minimumSwaps(arr):
    temp = {a: i for i, a in enumerate(arr)}
    swaps = 0
   #print(temp)
    for i in range(len(arr)):
        actual, expected = arr[i], i + 1
        actual_i, expected_i = i, temp[expected]
        if actual != expected:
            arr[actual_i] = expected
            arr[expected_i] = actual
            temp[actual] = expected_i
            temp[expected] = actual_i
            swaps += 1
    return swaps

s = '2 31 1 38 29 5 44 6 12 18 39 9 48 49 13 11 7 27 14 33 50 21 46 23 15 26 8 47 40 3 32 22 34 42 16 41 24 10 4 28 36 30 37 35 20 17 45 43 25 19'
arr = list(map(int, s.rstrip().split()))
#arr = [7, 6, 3, 2, 4, 5, 1]
print(minimumSwaps(arr))