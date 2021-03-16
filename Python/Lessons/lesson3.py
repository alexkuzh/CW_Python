class Dog():
    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " rolled over!")


# my_dog = Dog('Sharik',1)
# your_dog = Dog('Fox',10)
# # print(my_dog.name, my_dog.age)
# # my_dog.sit('dddddddd')
# # my_dog.roll_over()
# my_dog.age = 2
# print(your_dog.name)
# print(my_dog.name, my_dog.age)

# l = []
# for x in range(5):
#     m = Dog('dog'+str(x),x)
#     l.append(m)
#
# print(l[0].name,l[0].age,l[-1].name)
# l[3].sit()
# l[3].name = 'dog0'
# print(l[3].name, l[0].name)

class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = 2020
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' ' + str(
            self.odometer_reading)
        return long_name.title()

    def update_odometer(self, mileage):
        """Устанавливает заданное значение на одометре."""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles


# my_new_car = Car('audi', 'a4')
# my_new_car.odometr = 100
# my_new_car.update_odometer(500)
# print(my_new_car.get_descriptive_name())
# my_new_car.increment_odometer(100)
# print(my_new_car.get_descriptive_name())
# next_car = Car('ford','focus')
# # next_car.update_odometer(200)
# print(next_car.get_descriptive_name())

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model)
        self.charge = 100
        self.battery = Battery()

    def show_charge(self):
        self.charge = 80
        return self.charge

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' ' + str(
            self.odometer_reading) + ' ' + str(self.charge)
        return long_name.title()


class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


# car1 = Car('Ford', 'Focus')
# print(car1.get_descriptive_name())
# car2 = ElectricCar('Tesla', 'S3')
# print(car2.get_descriptive_name())
# # print(car2.show_charge())
# # print(car1)
# print(car2.get_descriptive_name())
# car2.battery.describe_battery()

# batt = Battery()
# batt.describe_battery()