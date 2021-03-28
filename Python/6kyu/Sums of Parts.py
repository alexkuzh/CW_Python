# https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/python
def parts_sums(ls):
    # your code
    a = []
    s = sum(ls)
    a.append(s)
    for i in range(len(ls)):
        s -= ls[i]
        a.append(s)
    return a


print(parts_sums([0, 1, 3, 6, 10]))
