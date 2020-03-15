# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
def find_outlier(integers):
    od = []
    ev = []
    for x in integers:
        if x % 2 == 1:
            od.append(x)
        else:
            ev.append(x)
    if len(od) == 1:
        return od[0]
    else:
        return ev[0]