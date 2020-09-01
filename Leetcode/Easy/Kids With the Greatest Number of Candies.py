# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
def kidsWithCandies(candies,extraCandies):
    m = max(candies)
    arr = []
    for x in candies:
        arr.append((x+extraCandies)>=m)
    return arr

print(kidsWithCandies([2,3,5,1,3],3))