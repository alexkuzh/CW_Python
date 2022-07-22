# https://www.codewars.com/kata/5a3af5b1ee1aaeabfe000084/train/python
import time

def check_1_sq(n):
    if (n**0.5).is_integer():
        return True
    return False


def check_2_sq(n):
    R = int(n**0.5)
    r = int(R*(2**0.5)/2)
    for x in range(r,R + 1):
        if ((n - x**2)**0.5).is_integer():
            return True
    return False

def check_3_sq(n):
    R = int(n**0.5)
    r = int(R*(2**0.5)/2)
    for x in range(r-1,R + 1):
        for y in range(x, R + 1):
            k = n - x**2 - y**2
            if k>0:
                if (k**0.5).is_integer():
                    return (True,[x,y,k**0.5])
    return False

def check_3_sq_1(n):
    if (n-1)%3 == 0:
        return True
    if (n-7)%8 > 0 and n%4==0:
        return False
    return True

def sum_of_squares(n):
    if check_1_sq(n):
        return 1
    if check_2_sq(n):
        return 2
    # if check_3_sq(n):
    #     return 3
    return 4

x = 1008
# x = 19
x = 3456
t1 = time.time()
# print(sum_of_squares(122131243))
# print(f'2 sq = {check_2_sq(x)}')
print(f'Short = {check_3_sq_1(x)}')
print(f'Long = {check_3_sq(x)}')
print(time.time()-t1)
# print(f'x=\t {x}  \t {sum_of_squares(x)} {sum_(x)}')

# print(math.log(8,2))