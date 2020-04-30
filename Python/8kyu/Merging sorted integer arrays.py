# https://www.codewars.com/kata/573f5c61e7752709df0005d2/train/python
def merge_arrays(first, second):
    # your code here
    return sorted(set(first+second))


print(merge_arrays([1, 3, 5], [2, 4, 6, 3]))