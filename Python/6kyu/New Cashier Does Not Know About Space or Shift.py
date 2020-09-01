# https://www.codewars.com/kata/5d23d89906f92a00267bb83d/train/python
def get_order(order):
    template = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']
    a = []
    for x in template:
        for i in range(order.lower().count(x.lower())):
            a.append(x)
    return ' '.join(a)


print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))