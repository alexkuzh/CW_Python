# https://www.codewars.com/kata/55c45be3b2079eccff00010f
import re
def order(sentence):
    # code here
    return '' if sentence == '' else \
        ' '.join([n[1] for n in sorted([re.findall('(\d+)', i) + [i] for i in sentence.split(' ')])])

sss = 'is2 Thi1s T4est 3a'
# print(order(sss))
# print([[i] for i in sss.split(' ')])
# print([re.findall('(\d+)', i) + [i] for i in sss.split(' ')])
# print(sorted([re.findall('(\d+)', i) + [i] for i in sss.split(' ')]))
# print([n[1] for n in sorted([re.findall('(\d+)', i) + [i] for i in sss.split(' ')])])

def order(words):
    return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

print(sorted('ewe1wer'))
print(order(sss))