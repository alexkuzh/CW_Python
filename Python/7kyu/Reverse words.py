# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
def reverse_words(text):
#go for it
    return ' '.join(x[::-1] for x in text.split(' '))