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



# h1 = Building(1, 'Новый')
# h2 = Building(1, 'Новый')
# h3 = Building(1, 'не новый')
# print(h1 == h2)
# print(h1 == h3)


# Объявите функцию single_root_words и напишите в ней параметры root_world и *other_words.
# Создайте внутри функции пустой список same_words, который пополнится нужными словами.
# При помощи цикла for переберите предполагаемо подходящие слова.
# Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
# После цикла верните образованный функцией список same_words.
# Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей занчение.

def single_root_words(root_world, *other_words):
    same_words = []
    for i in other_words:
        if root_world.lower() in i.lower():
            same_words.append(i)
        elif i.lower() in root_world.lower():
            same_words.append(i)
    print(same_words)








result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')