# https://www.hackerrank.com/test/33gp893pqhs/questions/ato4r93a7tb
def longestSubarray(arr):
    # Write your code here
    a = []
    for i in range(len(arr)-1):
        k=0
        for j in range(i,len(arr)):
            if abs(arr[i]-arr[j])<=1:
                k+=1
            else:
                break
        a.append(k)
    return max(a)


# print(longestSubarray([0, 1, 2, 1, 2, 3]))
print(longestSubarray([1, 1, 1, 3, 3, 2, 2]))
print(longestSubarray([2, 2, 1]))
