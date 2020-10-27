# https://www.codewars.com/kata/5518a860a73e708c0a000027/train/python
def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10
#
#
# def ld(d):
#     return int(str(d)[-1])
#
#
# def ld1(k, n):
#     if k in (0, 1, 5, 6):
#         return k
#     if n % 4 == 0:
#         return 6 if k % 2 else 1
#     arr = [[2, 6, 2, 4, 8], [3, 1, 3, 9, 7], [7, 1, 7, 9, 3], [8, 6, 8, 4, 2], [4, 6], [9, 1]]
#     for x in arr:
#         if x[0] == k:
#             if x[0] not in (4, 9):
#                 return x[n % 4 + 1]
#             elif x[0] == 9:
#                 return x[n % 2]
#             else:
#                 return x[not n % 2]
#
#
# def last_digit(lst):
#     # Your Code Here
#     if not lst: return 1
#     n = 1
#     while lst:
#         k = lst.pop()
#         n = ld1(ld(k), n)
#         print(k, n)
#     return n
#
#
# # for x in range(11):
# #     print(7**x)
# print((6 ** 6) % 10)
# print((6 ** 21) % 4)
# # print((7 ** (6 ** 21)) % 10)
# # print((7 ** ((6 ** 21) % 10)) % 10)
#
# # print(7**12)
# # k1 = 7
# # n1 = 12
# # print(ld1(k1, n1))
# # l1 = 3
# # print(k1 ** n1)
# # print(l1**5)
print(last_digit([7, 6, 21]))
