# https://leetcode.com/problems/maximum-subarray/
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
class Solution:
    def maxSubArray(nums: list) -> int:
        m = float('-inf')
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s > m:
                m = s
                #print(m)
            if s < 0:
                s = 0
        return m



print(Solution.maxSubArray([-2, 1, -2, 4, -1, 2, 1, -5, 14]))
# print([x+5 for x in [-2, 1, -3, 4, -1, 2, 1, -5, 4]])