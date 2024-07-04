# Входные данные
my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


# Выходные данные
# Дан список целых чисел, примените функции map и filter так, чтобы в конечном списке оставить нечётные квадраты чисел
# [1, 25, 49, 121, 1225, 7921]

def my_fun(x):
    return x ** 2


def my_filter(x):
    return x % 2


new_list = list(map(my_fun, my_list))

new_filter = filter(my_filter, new_list)
print(list(new_filter))
