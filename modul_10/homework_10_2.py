from time import sleep
from datetime import datetime
from threading import Thread

# Цель: научиться создавать классы наследованные от класса Thread.
#
# Задача "За честь и отвагу!":
# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# Атрибут name - имя рыцаря. (str)
# Атрибут power - сила рыцаря. (int)
# А также метод run, в котором рыцарь будет сражаться с врагами:
# При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
# После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
# Пункты задачи:
# Создайте класс Knight с соответствующими описанию свойствами.
# Создайте и запустите 2 потока на основе класса Knight.
# Выведите на экран строку об окончании битв.




class Knight(Thread):
    var = 100

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        day = 0
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.enemies -= self.power
            sleep(1)
            day += 1
            print(f'{self.name}, сражается {day} день(дня)..., осталось {self.enemies} воинов.')
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()



# import threading
# import time
#
# class Knight(threading.Thread):
#     def __init__(self, name, power):
#         super().__init__()
#         self.name = name
#         self.power = power
#         self.enemies = 100
#
#     def run(self):
#         print(f"{self.name}, на нас напали!")
#         start_time = time.time()
#         while self.enemies > 0:
#             self.enemies -= self.power
#             elapsed_time = time.time() - start_time
#             days = int(elapsed_time // 86400)
#             hours = int((elapsed_time % 86400) // 3600)
#             minutes = int((elapsed_time % 3600) // 60)
#             seconds = int(elapsed_time % 60)
#             print(f"{self.name} сражается {days} дней, {hours} часов, {minutes} минут, {seconds} секунд, осталось {self.enemies} воинов.")
#             time.sleep(1)
#         print(f"{self.name} одержал победу спустя {days} дней!")
#
# # Создаем объекты рыцарей
# knight1 = Knight("Женя", 50)
# knight2 = Knight("Алексей", 70)
#
# # Запускаем потоки рыцарей
# knight1.start()
# knight2.start()
