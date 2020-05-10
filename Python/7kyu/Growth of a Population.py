# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python
def nb_year(p0, percent, aug, p):
    # your code
    y = 0
    while p0 <= p:
        p0 += p0*percent/100 + aug
        y += 1
    return y

print(nb_year(1500, 5, 100, 5000))