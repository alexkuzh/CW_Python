def reverse(seq):
    # your code here
    a = list()
    for x in seq:
        a.insert(0,x)
    return a

print(reverse([5,4,3,2,1]))