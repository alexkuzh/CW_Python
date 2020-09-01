# https://leetcode.com/problems/two-sum/
import itertools
def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

print(solution(nums = [3,3], target = 6))
