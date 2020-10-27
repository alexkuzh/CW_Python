# https://www.codewars.com/kata/598d91785d4ce3ec4f000018/train/python
def calc_word(word):
    s = 0
    for x in word.lower():
        if x.isalpha():
            s += ord(x)-96
    return s

def name_value(my_list):
    r = []
    for i in range(len(my_list)):
        r.append(calc_word(my_list[i])*(i+1))
    return r



print(name_value(["codewars","abc","xyz"]))

1*3*5*3*7*9*5*11*3
2*2*2*2*2*2*2*2*2*2
3*3