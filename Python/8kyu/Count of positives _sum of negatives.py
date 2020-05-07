# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
def count_positives_sum_negatives(arr):
#your code here
    if arr:
        a = [0,0]
        for i in arr:
            if i > 0: a[0] += 1
            else: a[1] +=i
        return a
    else: return []

#    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []