# numbers = [1, 2, 3, 4, 5]
# cars = ['BMW', 'AUDI', 'VW', 'FORD', 'SCHEVI']
# for number in numbers:
#     print(number)
#
# for car in cars:
#     print(car.lower())

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
# print('*')
#
# for num in range(4):
#     print(num)
# s = range(5)
# print(type(s))
# l = list(s)
# print(type(l))
# print(l)
# print(list(range(10)))
# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for v in range(1,11):
#     # square = v ** 2
#     # squares.append(square)
#     squares.append(v**2)
# print(squares)
#
# print(min(squares))
# print(max(squares))
# print(sum(squares))
# print(sum(squares)/len(squares))

# list comprehension

# squares = [v ** 2 for v in range(1, 11)]
# print(squares)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# # print(players[::-1])
# print("Here are the first three players on my team:")
# for player in players[::-1]:
#     print(player.title())

# immutable
# dimensions = (200, 50)
# # dimensions[1] = 100
# dimensions = (200,100)
# print(dimensions[0])
# print(dimensions[1])

# players = ('charles', 'martina', 'michael', 'florence', 'eli')
# for n in players:
#     print(n)

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango",)
fruits2 = ('ddddd',)
fruits3 = ('ssssss')
# print(type(fruits2))
# print(type(fruits3))
# print(thislist[-4:-1])
# print(len(thislist))
# y = list(fruits)
# y[2] = 'cherry1'
# print(y)
# fruits = tuple(y)
# print(fruits)
# tuple3 = fruits + fruits2
# print(tuple3)

print(fruits.index('kiwi'))