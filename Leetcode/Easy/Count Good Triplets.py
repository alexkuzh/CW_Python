# https://leetcode.com/problems/count-good-triplets/
import itertools
def countGoodTriplets(arr, a, b, c):
    return len([x for x in itertools.combinations(arr, 3) if abs(x[0]-x[1])<=a and abs(x[1]-x[2])<=b and abs(x[0]-x[2])<=c])




print(countGoodTriplets(arr = [7,3,7,3,12,1,12,2,3], a = 5, b = 8, c = 1))