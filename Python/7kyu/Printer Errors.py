# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
import re
def printer_error(s):
# your code
    return str(len(re.findall(r"[n-z]",s)))+'/'+str(len(s))

print(printer_error('aaaxbbbbyyhwawiwjjjwwm'))