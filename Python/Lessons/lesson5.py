# def persistence(n):
#     i = 0
#     print(list(map(int,str(n))))
#     while n>9:
#         m = 1
#         for x in map(int,str(n)):
#             m *= x
#         n = m
#         print(n)
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


# print(persistence(234))
#
# def duplicate_encode(word):
#     s = ''
#     for x in word.lower():
#         if word.lower().count(x) == 1:
#             s += '('
#         else:
#             s += ')'
#     return s

# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# def duplicate_encode(word):
#     word = word.lower()
#     return ''.join('(' if word.count(x) == 1 else ')' for x in word)
#
#
# print(duplicate_encode('ssdf'))

