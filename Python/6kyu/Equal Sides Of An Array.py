# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python
def find_even_index(arr):
#your code here
    for i in range(1,len(arr)-1):
        if sum(arr[0:i]) == sum(arr[i+1:]): return i
    return -1

print(find_even_index([20,10,30,10,10,15,35]))