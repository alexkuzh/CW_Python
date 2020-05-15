# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
def sum_two_smallest_numbers(numbers):
#your code here
    return sum(sorted(numbers)[:2])


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))