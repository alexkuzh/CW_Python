# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
def spin_words(sentence):
    # Your code goes here
    sen = []
    for s in sentence.split(' '):
        sen.append(s[::-1]) if len(s)>=5 else sen.append(s)
    return ' '.join(sen)

print(spin_words('Welcome asdf'))