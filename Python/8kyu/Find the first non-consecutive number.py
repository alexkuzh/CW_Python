# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144
def first_non_consecutive(arr):
    #your code here
    i = arr[0]
    for x in arr:
        if i != x:
            return(x)
        i +=1
    return None