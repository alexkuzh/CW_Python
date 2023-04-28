# https://www.codewars.com/kata/60576b180aef19001bce494d/train/python
import math



def count_checkerboard(width, height, resolution):
    W = math.ceil(width//(resolution*2))
    H = math.ceil(height//(resolution*2))
    return (W, H)


print(count_checkerboard(11,6,5))