# Домашнее задание по уроку "Перегрузка операторов"
#
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новый класс Buiding
# Создайте инициализатор для класса Buiding,
# который будет задавать целочисленный атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашему заданию


class Building:
    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType



h1 = Building(1, 'Новый')
h2 = Building(1, 'Новый')
h3 = Building(1, 'не новый')
print(h1 == h2)
print(h1 == h3)
