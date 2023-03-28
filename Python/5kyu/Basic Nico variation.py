# https://www.codewars.com/kata/5968bb83c307f0bb86000015/train/python
import math

# Testing for 'cwjuklrahtf' and 'yorje'
# It should work for random inputs too: ' o j    e'
#                          should equal ' y  re   jo'

def nico(key, message):
    encoding_map = {}
    for i, char in enumerate(sorted(key)):
        encoding_map[char] = i
    map = []
    for x in key:
        map.append(encoding_map[x])
    print(map)
    s = ''
    message = message.ljust(len(key)*math.ceil(len(message)/len(key)))
    while message:
        l = dict(zip(list(map),message[:len(key)]))
        s += ''.join(dict(sorted(l.items(),key=lambda x:x[0])).values())
        message = message[len(key):]
    return s


print(nico("cwjuklrahtf", "yorje"))