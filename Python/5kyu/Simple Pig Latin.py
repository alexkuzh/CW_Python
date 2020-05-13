# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
def pig_it(text):
#your code here
    a = []
    for x in text.split(' '):
        a.append(x[1:]+x[0]+'ay') if len(x)>1 else a.append(x)
    return ' '.join(a)

print(pig_it('Pig latin is cool !'))
