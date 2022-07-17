# https://www.codewars.com/kata/5276c18121e20900c0000235/train/python

def find_missing_number(numbers):
    for x in range(1,len(numbers)+1):
        if x not in numbers:
            return x
    return max(numbers)+1


def find_missing_number1(numbers):
    s1 = set(numbers)
    s2 = set(range(1,max(numbers)+2))
    return list(s2 - s1)[0]


def find_missing_number2(numbers):
    if len(numbers) == max(numbers):
        return max(numbers)+1
    s1 = sum(numbers)
    s2 = sum(range(1,max(numbers)+1))
    return s2-s1


print(find_missing_number2([2, 3, 4]))
print(find_missing_number2([1, 2, 3]))