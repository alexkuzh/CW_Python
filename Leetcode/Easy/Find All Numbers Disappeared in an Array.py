# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
def findDisappearedNumbers(nums):
    n = sorted(set(nums))
    res = []
    print(n,'\n***************')
    for x in range(len(nums)-len(n)):
        n.append(0)
    for i in range(len(nums)):
        if n[i] != i+1:
            n.insert(i,i+1)
            res.append(i+1)
    print(n)



    return res

# print(findDisappearedNumbers([1,1]))
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))