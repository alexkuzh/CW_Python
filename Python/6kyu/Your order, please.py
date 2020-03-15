# https://www.codewars.com/kata/55c45be3b2079eccff00010f
import re
def order(sentence):
    # code here
    return '' if sentence == '' else ' '.join([n[1] for n in sorted([re.findall('(\d+)', i) + [i] for i in sentence.split(' ')])])
