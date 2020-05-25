# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
def tower_builder(n_floors):
    a = []
    for x in range(n_floors):
        a.append(' '*(n_floors-x)+'*'*(2*x+1)+' '*(n_floors-x))
        # print(' '*(n_floors-x)+'*'*(2*x+1)+' '*(n_floors-x))
    return a

print(tower_builder(9))