# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
def duplicate_count(text):
    # Your code goes here
    return sum([1 for x in set(text.lower()) if text.lower().count(x) > 1])

print(duplicate_count('aA11'))
