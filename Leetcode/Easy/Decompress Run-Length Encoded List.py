# https://leetcode.com/problems/decompress-run-length-encoded-list/   #1313
def make_arr(n,m):
    a = []
    for i in range(n):
        a.append(m)
    return a

def decompressRLElist(nums):
    a = []
    for i in range(0,len(nums),2):
        a += make_arr(nums[i],nums[i+1])
    return a




print(decompressRLElist([1,2,3,4]))