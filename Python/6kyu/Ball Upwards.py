# https://www.codewars.com/kata/566be96bb3174e155300001b/train/python
def max_ball(v0):
# your code
    # g = 9.81
    # v - g * t = 0
    # t = v/g
    # v = v0 / 3.6
    # print(v0/3.6/9.8*10)
    return round(v0/3.6/9.8*10)

print(max_ball(45))