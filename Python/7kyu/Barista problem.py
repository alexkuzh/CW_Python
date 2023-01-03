#https://www.codewars.com/kata/6167e70fc9bd9b00565ffa4e/train/python

def barista(coffees):
    r = [0]
    m = 0
    coffees.sort()
    for i in range(len(coffees)):
        r.append(r[-1]+coffees[i] + m)
        print(r)
        m=2
    return sum(r)

# b = [2, 3, 5, 9, 10]
# b = [5,20]
b = [20,5,4,3,1,5,7,8]

print(barista(b))