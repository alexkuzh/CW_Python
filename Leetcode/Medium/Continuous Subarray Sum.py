# https://leetcode.com/problems/continuous-subarray-sum/
'''not solved'''

def checkSubarraySum(nums, k):
    # l = []
    # for i in range(len(nums)):
    #     l.append(nums[i] % k)
    # print(l)
    if k == 0:
        if sum(nums) ==0 and len(nums)>1:
            return True
        return False
    if k >len(nums):
        for _ in range(k):
            nums.append(0)
    i = 0
    while i < len(nums) - k:
        for n in range(2, 6):
            if sum(nums[i:i + n]) % 6 == 0:
                print(nums[i:i + n], sum(nums[i:i + n]))
                return True
    return False


print(checkSubarraySum([0,0], 0))
