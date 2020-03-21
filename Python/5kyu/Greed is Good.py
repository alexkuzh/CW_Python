#https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python
def score(dice):
    obj = [['111',1000], ['666',600], ['555', 500], ['444',400], ['333',300], ['222',200], ['1',100], ['5',50]]
    s = ''.join(str(x) for x in (sorted(dice)))
    a = 0
    for i in range(0, 5):
        for j in range(0, 8):
            if s.find(obj[j][0]) >= 0:
                a += obj[j][1]
                s = s.replace(obj[j][0], '', 1)
    return a

print(score([1, 5, 1, 3, 4]))