# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
import re


def validate_pin(pin):
    # return true or false
    p = re.findall(r"(^\d{6})|(^\d{4})", pin)
    if p:
        return max(p[0]) == pin
    return False

print(validate_pin('1234'))
