# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python
def tickets(people):
    kassa = []
    res = 'YES'
    while people:
        x = people.pop(0)
        if x == 25:
            kassa.append(x)
            res = 'YES'
        if x == 50:
            if kassa.count(25) >0:
                kassa.remove(25)
                kassa.append(x)
                res = 'YES'
                continue
            return 'NO'
        if x == 100:
            if kassa.count(25) >= 1 and kassa.count(50) >= 1:
                kassa.remove(25)
                kassa.remove(50)
                kassa.append(x)
                res = 'YES'
                continue
            if kassa.count(25) >= 3:
                kassa.remove(25)
                kassa.remove(25)
                kassa.remove(25)
                kassa.append(x)
                res = 'YES'
                continue
            return 'NO'
    return res

print(tickets([25, 25, 25, 25, 50, 100, 50]))