# Применить dunder методы iter, next в своём классе
# Задание
# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне. При создании и инициализации объекта этого класса создаются атрибуты:
# start – начальное значение (если значение не передано, то 0)
# end – конечное значение (если значение не передано, то 1)
# Примечание
# Значение атрибута start всегда меньше значения атрибута end
# В решении задачи не использовать list, tuple и др. встроенные типы данных.
# Входные данные
# en = EvenNumbers(10, 25)
# for i in en:
# print(i)
# Выходные данные
# После перебора и вывода:
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24

class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        even_number = self.current
        self.current += 2
        return even_number


en = EvenNumbers(start=10, end=25)
for num in en:
    print(num)
