#   https://www.codewars.com/kata/opposites-attract/train/python
def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2 == 1


print(lovefunc(1, 4))
