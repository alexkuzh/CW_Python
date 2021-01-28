# https://www.codewars.com/kata/5aa1bcda373c2eb596000112/solutions/python
'''Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .
1. Функция
2. Список
3. Множество
4. Срез
5. Методы списка
    5.1. Сортировка
    5.2. Сумма
'''
def max_tri_sum(l):
    # s= set(l)
    # print(s)
    # s = sorted(s)
    # print(s)
    # print(s[-3:])
    return sum(sorted(set(l))[-3:])

l1 = [1,2,5,4,3,2,7,3,3,6,]
# s = set(l1)
# print(s)
# print(l1[-4:])
# print(sorted(l1))
# print(max(l1))
print(max_tri_sum(l1))
