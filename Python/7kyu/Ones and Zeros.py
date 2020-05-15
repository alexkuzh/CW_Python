# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
def binary_array_to_number(arr):
# your code
    return int(''.join([str(elem) for elem in arr]),2)
print(binary_array_to_number([1,0,0]))