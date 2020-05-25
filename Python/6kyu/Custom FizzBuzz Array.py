# https://www.codewars.com/kata/5355a811a93a501adf000ab7/train/python
def fizz_buzz_custom(string_one='Fizz', string_two='Buzz', num_one=3, num_two=5):
    # your code here
    a = []
    for i in range (1,101):
        st = ''
        if i % num_one == 0: st += string_one
        if i % num_two == 0: st += string_two
        if st == '': a.append(i)
        else: a.append(st)
    return a


print(fizz_buzz_custom("Fizz","Buzz",2,3))
# print(fizz_buzz_custom())