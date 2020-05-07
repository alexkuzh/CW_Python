# https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
def sum_array(arr):
#your code here
    return sum(arr) - max(arr) - min(arr) if arr and len(arr) > 1 else 0


print(sum_array([6, 2, 1, 8, 10]))