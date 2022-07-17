# https://www.hackerrank.com/challenges/polar-coordinates/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
import cmath


def out(st):
    r = complex(st).real
    i = complex(st).imag
    ph = cmath.phase(complex(r,i))
    z = abs(complex(r,i))
    print(f'{z}\n{ph}')

# s = complex('1+2j')
out(input())