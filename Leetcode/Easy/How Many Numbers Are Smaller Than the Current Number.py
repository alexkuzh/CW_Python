# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/ #1365
def smallerNumbersThanCurrent(nums):
    a = []
    for x in nums:
        a.append(len([m for m in nums if m < x]))
    return a


print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
