# https://www.codewars.com/kata/5715eaedb436cf5606000381/python
def positive_sum(arr):
    # Your code here
    return sum([x for x in arr if x > 0])

print(positive_sum([-1,2,3,4,-5]))