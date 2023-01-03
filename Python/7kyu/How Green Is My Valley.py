# https://www.codewars.com/kata/56e3cd1d93c3d940e50006a4/train/python

def make_valley(arr):
    r = []
    arr.sort()
    if len(arr) % 2:
        r.append(arr[0])
        arr.pop(0)
    for i in range(len(arr)//2):
        r.append(arr[2*i])
        r.insert(0,arr[2*i+1])
    return r

print(make_valley([17, 15, 14, 8, 7, 7, 5, 4, 4, 1]))