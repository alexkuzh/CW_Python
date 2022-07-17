# https://www.codewars.com/kata/57f24e6a18e9fad8eb000296/train/python

def how_much_i_love_you(nb_petals):
    # your code
    a = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    print(3%6)
    return a[nb_petals%6-1]

print(how_much_i_love_you(3))