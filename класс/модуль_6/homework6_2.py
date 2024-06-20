# Доступ к свойствам родителя. Переопределение свойств

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = self.set_color(color)

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def set_color(self, new_color):
        if new_color.lower() not in self.__COLOR_VARIANTS:
            print(f'Нельзя сменить цвет на: {new_color}')
        else:
            self.__color = new_color
            return self.__color

    def print_info(self):
        return f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}\n'


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, engine_power, color, limit):
        super().__init__(owner, model, engine_power, color)
        self.limit = self.sedan_passengers(limit)

    def sedan_passengers(self, limit):
        if Sedan.__PASSENGERS_LIMIT != limit:
            return f'В седане только 5 мест'
        else:
            self.limit = limit
            return self.limit


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue', 4)
print(vehicle1.print_info())
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print(vehicle1.print_info())
print('*' * 20)
print(vehicle1.limit)
