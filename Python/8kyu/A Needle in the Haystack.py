# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
def find_needle(haystack):
    return "found the needle at position {}".format(haystack.index('needle'))

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))