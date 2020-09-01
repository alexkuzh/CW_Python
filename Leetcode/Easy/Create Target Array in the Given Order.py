# https://leetcode.com/problems/create-target-array-in-the-given-order/
# 1389
def createTargetArray(nums, index):
    a = []
    for i in range(len(nums)):
        a.insert(index[i],nums[i])
    return a

print(createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
