# Задание: Декораторы в Python
#
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11

def is_prime(func):
    def wrapper(*args, **kwargs):
        original = func(*args, **kwargs)
        if original <= 1:
            return f'Составное число\n{original}'
        for i in range(2, int(original ** 0.5) + 1):
            if original % i == 0:
                return f'Составное число\n{original}'
        return f'Простое число\n{original}'
    return wrapper


@is_prime
def sum_tree(a, b, c):
    res = a + b + c
    return res


# Простое число
result = sum_tree(2, 3, 6)
print(result)
# Составное число
result = sum_tree(3, 3, 6)
print(result)
