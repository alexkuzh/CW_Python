# https://www.codewars.com/kata/57c7231c484cf9e6ac000090/train/python

def sum_arrays(arrays, shift):
    a = [[0] * (i * shift) + arrays[i] + [0] * (shift * (len(arrays) - i - 1)) for i in range(len(arrays))]
    # a = []
    # for i in range(len(arrays)):
    #     ar = [0] * (i * shift) + arrays[i] + [0] * (shift * (len(arrays) - i - 1))
    #     a.append(ar)
    #     print(ar)
    return list(map(sum, zip(*a)))



#print(sum_arrays([[1, 2, 3, 4, 5, 6], [7, 7, 7, -7, 7, 7], [1, 1, 1, 1, 1, 1]], 3))
#print(sum_arrays([[1, 2, 3, 4, 5, 6], [7, 7, 7, 7, 7, -7]], 0))
print(sum_arrays([[1, 2, 3, 4, 5, 6], [7, 7, 7, 7, 7, 7]], 3))