# https://www.codewars.com/kata/597d75744f4190857a00008d/train/python

def paint_letterboxes(start, finish):
    d = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for i in range(start,finish+1):
        for h in str(i):
            d[h] +=1
    return list(d.values())



print(paint_letterboxes(125,132))