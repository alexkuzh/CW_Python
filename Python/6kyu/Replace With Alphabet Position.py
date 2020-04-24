# https://www.codewars.com/kata/546f922b54af40e1e90001da/python

def alphabet_position(text):
    text = text.lower()
    s = ''
    for x in text:
        if ord(x)>=97 and ord(x)<=97+26:
            s = s + str(ord(x)-96) +' '
    return s.strip()


print(alphabet_position("The sunset sets at twelve o' clock."))