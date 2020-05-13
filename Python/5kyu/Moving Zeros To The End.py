# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
def move_zeros(array):
    # your code here
    a1,az = [],[]
    for x in range(0,len(array)):
        az.append(0) if (type(array[x]) == int or type(array[x]) == float) and array[x] == 0 else a1.append(array[x])
    return a1+az


# print(move_zeros([0, 1, None, 2, False, 1, 0]))
# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))