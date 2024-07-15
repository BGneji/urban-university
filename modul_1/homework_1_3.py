# Практическая работа по уроку "Динамическая типизация"
#
# Цель: Написать программу на языке Python, используя Pycharm, для демонстрации динамической типизации.
#
# В проекте, где вы решаете домашние задания, создайте модуль 'homework3.py' и напишите весь код в нём.
#
# 2. Создайте переменные разных типов данных:
#   - Создайте переменную name и присвойте ей значение вашего имени (строка).
#   - Выведите значение переменной name на экран.
#   - Создайте переменную age и присвойте ей значение вашего возраста (целое число).
#   - Выведите значение переменной age на экран.
#   - Перезапишите в age текущее значение переменной age + новое.
# Как неверно (просто перезапись на новое число):
# a = 15
# a = 17
#   - Выведите измененное значение переменной age на экран.
#   - Создайте переменную is_student и присвойте ей значение True (логическое значение).
#   - Выведите значение переменной is_student на экран.
#
# Примечания:
# - Для вывода значений на экран используйте функцию print().
# - Обратите внимание на использование разных типов данных и возможности их изменения.
#
# Пример результата выполнения программы:
# Name: John
# Age: 25
# New Age: 26
# Is Student: True

name = "Aleksey"
print('Name: ' + name)
age = 25
print(f'Age: {age}')
age += 10
print(f'New age: {age}')
is_student = True
print(f'Is_student: {is_student}')