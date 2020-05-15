# https://www.codewars.com/kata/5813d19765d81c592200001a/train/python
def dont_give_me_five(start,end):
    # your code here
    return len([x for x in range(start,end+1) if '5' not in str(x)])

print(dont_give_me_five(1,9))