# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
def findNumbers(nums):
    return len([x for x in nums if not len(str(x))%2])



print(findNumbers(nums = [12,345,2,6,7896]))
