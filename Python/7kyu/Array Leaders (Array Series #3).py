# https://www.codewars.com/kata/5a651865fd56cb55760000e0/train/python

def array_leaders(numbers):
    a = []
    for i in range(len(numbers)):
        if numbers[i] > sum(numbers[i+1:]):
            a.append(numbers[i])
    return a

def array_leaders1(numbers):
    a = [numbers[i] for i in range(len(numbers)) if numbers[i] > sum(numbers[i+1:])]
    return a


print(array_leaders1([16,17,4,3,5,2]))