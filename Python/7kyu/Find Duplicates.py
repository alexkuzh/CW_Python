# https://www.codewars.com/kata/5558cc216a7a231ac9000022
def duplicates(array):
    #your code here
    was = set(filter(lambda x: array.count(x)>1, array))
    l = []
    print(was)
    for a in was:
        array.pop(array.index(a))
    for a in array:
        if a in was and a not in l:
            l.append(a)
    return l

print(duplicates([1, 2, 4, 4, 4, 3, 3, 1, 5, 3, '5']))