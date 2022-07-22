# https://www.codewars.com/kata/563f879ecbb8fcab31000041/train/python
def factory(x):
    # Good Luck!
    return lambda n: [x*i for i in n]


my_arr = [1, 2, 3]
threes = factory(3)
print(threes(my_arr))