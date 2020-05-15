# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python
def first_non_repeating_letter(string):
#your code here
    if len(string)<=1: return string
    for i in range(0,len(string)):
        if string.lower().count(string[i].lower())==1:
            return string[i]

print(first_non_repeating_letter('moonmen'))