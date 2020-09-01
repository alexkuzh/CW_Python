# https://www.codewars.com/kata/5efae11e2d12df00331f91a6/train/python
import random
import hashlib

def crack(hash):
# G00D LUCK
    for x in range(99999):
        if hashlib.md5(str(x).zfill(5).encode()).hexdigest() == hash:
            return str(x).zfill(5)
    return 'I can`t crack'

print(crack("827ccb0eea8a706c4c34a16891f84e7b"))