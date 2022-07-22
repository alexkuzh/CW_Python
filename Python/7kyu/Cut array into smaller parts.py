# https://www.codewars.com/kata/58ac59d21c9e1d7dc5000150/train/python
def make_parts(arr, chunkSize):
    d=[]
    while arr:
        d.append(arr[:chunkSize])
        arr = arr[chunkSize:]
    return d

print(make_parts([1,2,3,4,5], 2))