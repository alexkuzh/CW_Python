# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def removeDuplicates(nums):
    return len(set(nums))

print(removeDuplicates([1,1,2]))