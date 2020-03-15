# https://www.codewars.com/kata/52b7ed099cdc285c300001cd
def sum_of_intervals(intervals):
    l = [list(x) for x in sorted(intervals)]
    a = []
    a.append(l.pop(0))
    while len(l) > 0:
        if (l[0][0] <= a[-1][1]) and (l[0][1] >= a[-1][1]):
            a[-1][1] = l[0][1]
            l.pop(0)
        elif l[0][0] <= a[-1][1] and l[0][1] <= a[-1][1]:
            l.pop(0)
        else:
            a.append(l.pop(0))
    s = sum(x[1] - x[0] for x in a)
    return s
