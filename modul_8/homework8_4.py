# Задача:
# Напишите функцию-генератор all_variants(text), которая принимает строку text и
# возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.
# Пример результата выполнения программы:
# Пример работы функции:
# a = all_variants("abc")
# for i in a:
# print(i)
# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc


def all_variants(text):
    for i in range(len(text)):
        yield text[i]
        for j in range(2 + i, len(text) + 1):
            yield text[i:j]


a = all_variants("abc")
for el in a:
    print(el)
