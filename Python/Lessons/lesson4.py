# def persistence(n):
#     i = 0
#     while n>9:
#         m = 1
#         for x in map(int,str(n)):
#             m *= x
#         n = m
#         i += 1
#     return i

# def persistence(n):
#     n = str(n)
#     count = 0
#     while len(n) > 1:
#         p = 1
#         for i in n:
#             p *= int(i)
#         n = str(p)
#         count += 1
#     return count

# def persistence(n):
#     nums = [int(x) for x in str(n)]
#     sist = 0
#     while len(nums) > 1:
#         newNum = nums.reduce(lambda x, y: x * y, nums)
#         nums = [int(x) for x in str(newNum)]
#         sist = sist + 1
#     return sist
#
# print(persistence(39))

# def duplicate_encode(word):
#     s = ''
#     for x in word.lower():
#         if word.lower().count(x) == 1:
#             s += '('
#         else:
#             s += ')'
#     return s
#
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# def duplicate_encode(word):
#     word = word.lower()
#     return ''.join('(' if word.count(x) == 1 else ')' for x in word)

# print(duplicate_encode('wertdesw'))

# def is_valid_walk(walk):
#     #determine if walk is valid
#     n = walk.count('n')
#     s = walk.count('s')
#     w = walk.count('w')
#     e = walk.count('e')
#     return n==s and w==e and len(walk) == 10


# def isValidWalk(walk):
#     return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

# def isValidWalk(walk):
#     if len(walk) != 10:
#         return False
#     x, y = 0, 0
#     for direction in walk:
#         if direction == 'n':
#             y += 1
#         elif direction == 's':
#             y -= 1
#         elif direction == 'e':
#             x += 1
#         elif direction == 'w':
#             x -= 1
#         else:
#             return False
#
#     return x == 0 and y == 0

# def song_decoder(song):
#     return ' '.join(list(filter(lambda a: a != '', song.split('WUB'))))

# song = "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"
# print(song.split('WUB'))
# print(list(filter(lambda a: a != '', song.split('WUB'))))
# print(song_decoder(song))

# def song_decoder(song):
#     return " ".join(song.replace('WUB', ' ').split())
# print(song.replace('WUB', ' '))
# print(song.replace('WUB', ' ').split())

# def song_decoder(song):
#     return ' '.join([a for a in song.split('WUB') if a])

# def tribonacci(signature, n):
#     #your code here
#     if n == 0: return []
#     if n == 1: return signature[:1]
#     if n == 2: return signature[:2]
#     i = 3
#     a = signature
#     while i < n:
#         a.append(sum(a[-3:]))
#         i += 1
#     return a
#
# def tribonacci(signature, n):
#     res = signature[:n]
#     for i in range(n - 3):
#         res.append(sum(res[-3:]))
#     return res
#
# def tribonacci(signature,n):
#     a,b,c = signature
#     result = []
#     for i in range(n):
#         result.append(a)
#         a,b,c = b,c,a+b+c
#     return result

# print(tribonacci([1, 1, 1], 10))

# def alphabet_position(text):
#     text = text.lower()
#     s = ''
#     for x in text:
#         if ord(x)>=97 and ord(x)<=97+26:
#             s = s + str(ord(x)-96) +' '
#     return s.strip()

# def alphabet_position(s):
#     return " ".join(str(ord(c)-ord("b")) for c in s.lower() if c.isalpha())

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# def alphabet_position(text):
#     if type(text) == str:
#         text = text.lower()
#         result = ''
#         for letter in text:
#             if letter.isalpha() == True:
#                 result = result + ' ' + str(alphabet.index(letter) + 1)
#         return result.lstrip(' ')

# def alphabet_position(text):
#     alphabet = {  'a' : 1,'b' : 2,'c' : 3,'d' : 4,'e' : 5,'f' : 6,'g' : 7,'h' : 8,'i' : 9,'j' : 10,'k' : 11,'l' : 12,'m' : 13,                  'n' : 14,'o' : 15,'p' : 16,'q' : 17,'r' :18,'s' : 19,'t' : 20,'u' : 21,'v' : 22,'w' : 23,'x' : 24,'y' : 25,'z' : 26, }
#     inds = []
#     for x in text.lower():
#         if x in alphabet:
#             inds.append(alphabet[x])
#     return ' '.join(([str(x) for x in inds]))

# import re
# def order(sentence):
#     # code here
#     return '' if sentence == '' else ' '.join([n[1] for n in sorted([re.findall('(\d+)', i) + [i] for i in sentence.split(' ')])])
#
# s = "is2 Thi1s T4est 3a"
# print([[i] for i in s.split(' ')])
# print(sorted([re.findall('(\d+)', i) + [i] for i in s.split(' ')]))
# print([n[1] for n in sorted([re.findall('(\d+)', i) + [i] for i in s.split(' ')])])
# print(order(s))
# def extract_number(word):
#     for l in word:
#         if l.isdigit(): return int(l)
#     return None
#
# def order(sentence):
#     return ' '.join(sorted(sentence.split(), key=extract_number))
#
# def order(words):
#     return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))


# def namelist(d):
#     if d == []: return ''
#     l = [x.get('name') for x in d]
#     if len(l) == 1: return l[0]
#     return ', '.join(l[:-1]) + ' & ' + l[-1]

# # print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
# def namelist(names):
#     if len(names) > 1:
#         return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
#                                 names[-1]['name'])
#     elif names:
#         return names[0]['name']
#     else:
#         return ''


def to_camel_case(text):
    #your code here
    return text[0]+''.join([x.capitalize() for x in text.replace('_', '-').split('-')])[1:]
text = "the-stealth_warrior"
# print(text.replace('_', '-').split('-'))
# print(''.join([x.capitalize() for x in text.replace('_', '-').split('-')]))
# print(to_camel_case(text))
#
# def to_camel_case(s):
#     return s[0] + s.title().translate(None, "-_")[1:] if s else s
#
# print(text.title())