# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
def find_short(s):
    # your code here
    a = s.split(' ')
    a.sort(key = len)
    return len(a[0])

#     return len(min(s.split(' '), key=len))
print(find_short("bitcoin take over the world maybe who knows perhaps"))