# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# # print("The number " + str(number) + " is odd." if number % 2 else "The number " + str(number) + " is even.")
# print(["even","odd"][number % 2])
# # if number % 2:
# #     print("\nThe number " + str(number) + " is odd.")
# # else:
# #     print("\nThe number " + str(number) + " is even.")
# current_number: int = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
# print('end')
# flag = True
# print('Enter "quit" to end program')
# message = ''
#
# while True:
#     message = input('tell me about yourself')
#     if message == 'quit':
#         # flag = False
#         break
#     else:
#         print(message)
# print('end')

# break

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# x = 1
# while x <= 5:
#     print(x)
#     # x += 1

# unconfirmed_users = ['alice', 'bob', 'eva']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
#
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
#
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# d = {} #dictionary
# l = [] #list
# t = () #tuple
# d =  {'color': 'green', 3: 5}
# print(d)
# d['23'] = 'wwww'
# print(d)
# # d['23'] = 'eeeeeee'
# del d['23']
# print(d)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# # print(favorite_languages['jen'])
# for name, lang in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#           lang.title() + ".")
# print()
# # for name in favorite_languages.keys():
# for name in favorite_languages:
#     print(name.title() + "'s favorite language is " +
#             favorite_languages[name].title() + ".")

# friends = ['phil', 'sarah']
# for name in sorted(favorite_languages):
#     print(name.title())
#     # if name in friends:
#     #     print(" Hi " + name.title() + ", I see your favorite language is " +
# 	#             favorite_languages[name].title() + "!")

# for name in favorite_languages.keys():
# for v in sorted(set(favorite_languages.values())):
#     print(v)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = []
for alien_num in range(10):
    new_alien = {'color': 'red', 'points': 15}
    aliens.append(new_alien)

print(aliens)