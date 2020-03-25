# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
def filter_list(l):
    'return a new list with the strings filtered out'
    return list(filter(lambda x: type(x) == int, l))

print(filter_list([1, 2, 'a', 'b']))