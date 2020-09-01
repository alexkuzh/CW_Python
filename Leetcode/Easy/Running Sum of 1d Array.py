# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List

class Solution:
    def runningSum(nums: List[int]) -> List[int]:
        arr = []
        a = 0
        for i in nums:
            a += i
            arr.append(a)
        return arr

print(Solution.runningSum([1,2,3,4]))