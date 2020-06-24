# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
def to_camel_case(text):
    #your code here
    return text[0]+''.join([x.capitalize() for x in text.replace('_', '-').split('-')])[1:]

text = 'the#stealth-warrior'

print(to_camel_case(text))


print(text[:1] + text.title()[1:])