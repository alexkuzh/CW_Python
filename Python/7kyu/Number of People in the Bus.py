# https://www.codewars.com/kata/5648b12ce68d9daa6b000099
def number(bus_stops):
    a = 0
    for x in bus_stops:
        a = a + x[0] - x[1]
        if a<0: return None
    return a