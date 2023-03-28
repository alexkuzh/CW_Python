# https://www.codewars.com/kata/563fb342f47611dae800003c/train/python

def trim(string, max_length):
    if len(string) <= max_length:
        return string
    else:
        if len(string) <= 3:
            return string[:max_length] + "..."
        else:
            return string[:max_length-3] + "..."


print(trim("XWxM", 3))

