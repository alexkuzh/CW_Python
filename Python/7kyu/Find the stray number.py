# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
def stray(arr):
    a = sorted(arr)
    return a[-1] if a[len(arr)//2] == a[0] else a[0]