# Цель: понять как работают потоки на практике, решив задачу
#
# Задача "Потоковая запись в файлы":
# Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов,
# file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>"
# в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её:
# from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
#
# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.
#
# Пример результата выполнения программы:
# Алгоритм работы кода:
# # Импорты необходимых модулей и функций
# # Объявление функции write_words
# # Взятие текущего времени
# # Запуск функций с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы функций
# # Взятие текущего времени
# # Создание и запуск потоков с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы потоков
# Вывод на консоль:
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411 # Может быть другое время
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575 # Может быть другое время


from time import sleep
from datetime import datetime
from threading import Thread

start_time = datetime.now()


def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        text = f'Какое-то слово № {i}'
        with open(f'{file_name}.txt', 'a', encoding='utf-8') as file:
            file.write(text + '\n')
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.txt')


wite_words(10, 'example1')
wite_words(30, 'example2')
wite_words(200, 'example3')
wite_words(100, 'example4')

end_time = datetime.now()
res_time = end_time - start_time
print(f'Работа потоков', res_time)

start_time = datetime.now()

thr_first = Thread(target=wite_words, args=(10, 'example5'))
thr_second = Thread(target=wite_words, args=(30, 'example6'))
thr_third = Thread(target=wite_words, args=(200, 'example7'))
thr_four = Thread(target=wite_words, args=(100, 'example8'))

# запуск потоков
thr_first.start()
thr_second.start()
thr_third.start()
thr_four.start()

# обязательно дождаться окончания отработки потока
thr_first.join()
thr_second.join()
thr_third.join()
thr_four.join()

end_time = datetime.now()
res_time = end_time - start_time
print(f'Работа потоков', res_time)
