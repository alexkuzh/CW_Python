# https://www.codewars.com/kata/53697be005f803751e0015aa/train/python
def encode(st):
    return st.replace('a','1').replace('e','2').replace('i','3').replace('o','4').replace('u','5')

def decode(st):
    return st.replace('1','a').replace('2','e').replace('3','i').replace('4','o').replace('5','u')


print(encode('hello'))