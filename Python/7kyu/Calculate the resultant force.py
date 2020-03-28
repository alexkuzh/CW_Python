# https://www.codewars.com/kata/5b707fbc8adeaee7ac00000c
import math
def solution(force1, force2, theta) :
    r = math.radians(theta)
    x = force1 + force2 * math.cos(r)
    y = force2 * math.sin(r)
    return math.hypot(x, y), math.degrees(math.atan2(y, x))


print(solution(20, 10, 120))