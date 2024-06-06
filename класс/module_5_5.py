# Создайте новый проект или продолжите работу в текущем проекте
#
# Ваша задача:
# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и
# функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
# а также переопределите функцию horse_powers
# Создайте экземпляр класса Nissan и распечайте через функцию print vehicle_type, price
# Получившийся код прикрепите к заданию текстом

class Vehicle:
    def __init__(self):
        self.vehicle_type = 'none'


class Car:

    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return 'Лошадиная сила'


class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 2000
        self.vehicle_type = 'Nissan'


n = Nissan()
print('Марка машины: ', n.vehicle_type, 'цена: ', n.price)
