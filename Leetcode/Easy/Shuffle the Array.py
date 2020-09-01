# https://leetcode.com/problems/shuffle-the-array/
def shuffle(nums,n):
    a1 = nums[:n]
    a2 = nums[n:]
    r = str(list(zip(a1,a2))).replace('(','').replace(')','').replace(' ','').replace('[','').replace(']','').split(',')
    return r


print(shuffle([1,2,3,4],2))