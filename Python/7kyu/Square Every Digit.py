# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
def square_digits(num):
    s = ''
    for x in str(num):
        s += str(int(x)**2)
    return int(s)

print(square_digits(9119))