# https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python
def row_weights(array):
    # your code here
    a = sum([array[i] for i in range(len(array)) if i % 2 == 0])
    b = sum(array) - a
    return (a,b)

print(row_weights([13,27,49]))

'a'
'webbrowserccc'
'ddddd'


