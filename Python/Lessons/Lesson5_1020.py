# if
# cars = ['bmw','audi','subaru','toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
#
# car = 'bmw'
# car1 = 'BMW'
# print(car == car1)
# age = 30
# print(age > 31)
# answer = 17
# if answer == 42:
#     print("That is not the correct answer. Please try again!")
# else:
#     print('Noooo!')

# a = 10
# b = 20
# print('a>5',a>5)
# print('b>5',b>5)
# print(a>5, 'and' ,b >5 ,'=', a>5 and b >5)

# True and True and True = True
# False and True = False
# True and False = False
# False and False = False

# or
# a = 10
# b = 20
# print(a>5, 'or' ,b <5 ,'=', a>5 or b <5)

# True or True  = True
# False or True = True
# True or False = True
# False or False = False

# cars = ['bmw','audi','subaru','toyota']
# car = 'bmw'
# if car not in cars:
#     print('it`s a new car')
# else:
#     print('the car is in the list')
#     print('ffffffff')
#     for i in range(5):
#         print(i)

# if xxx:
#     ddd1
# elif xxx1:
#     ddd2
# elif xxx2:
#     ddd3
# else:
#     ddd4

# age = 19
# if age <4:
#     print('your cost is 0')
# elif age <18:
#     print('your cost is 5')
# elif age >19:
#     print('your cost is 10')
# else:
#     print(age)
# print('next')

# cars = ['bmw','audi','subaru','toyota']
# if 'bmw' in cars:
#     print('BMW exists')
# if 'audi' in cars:
#     print('AUDI exists')

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print("Adding " + requested_topping + ".")
# print("\nFinished making your pizza!")

# requested_toppings = []
# if requested_toppings:
#     print('Not Empty')
# else:
#     print('Empty')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

age = 3
if age < 4:
    print('''''')
