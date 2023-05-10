# https://www.codewars.com/kata/57a93f93bb9944516d0000c1/train/python
class Dictionary():

    def __init__(self):
        # Your code
        self.d = dict()

    def newentry(self, word, definition):
        # Your code
        self.d[word] = definition

    def look(self, key):
        # your code
        return self.d.setdefault(key, f"Can't find entry for {key}")


d = Dictionary()
d.newentry('s','ddd')
d.newentry('s1','ddd2')
print(d.look('s2'))
