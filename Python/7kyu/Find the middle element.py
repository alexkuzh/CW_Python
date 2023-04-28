# https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python

def gimme(a):
    # Implement this function
    for i in range(len(a)):
        if a[i] != min(a) and a[i] != max(a):
            return i

def gimme(inputArray):
    # Implement this function
    return inputArray.index(sorted(inputArray)[1])