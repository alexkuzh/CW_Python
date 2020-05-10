# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
def is_isogram(string):
    #your code here
    return len(list(string)) == len(set(string.lower()))