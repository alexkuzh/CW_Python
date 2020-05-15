# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python
def remove_smallest(numbers):
    a = numbers.copy()
    a.remove(min(numbers))
    return a


print(remove_smallest([1, 2, 3, 4, 5]))