import threading
from threading import Thread
from time import sleep
import queue


class Table:
    def __init__(self, number: int):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue
        self.tables = tables

    #  моделирует приход посетителя(каждую секунду).
    def customer_arrival(self):
        count = 1
        while count < 11:
            customer = Customer(count, self)
            print(f'Посетитель номер {count} прибыл')
            customer.start()
            count += 1
            sleep(1)

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {customer} сел за стол  {table.number}')
                sleep(5)
                print(f'Посетитель номер {customer} покушал и ушел')
                table.is_busy = False
                self.check_queue()
                break
        else:
            self.queue.put(customer)
            print(f'Посетитель номер {customer} ожидает свободный стол')

    def check_queue(self):
        if not self.queue.empty():
            customer = self.queue.get()
            self.serve_customer(customer)


class Customer(Thread):
    def __init__(self, number, cafe):
        self.number = number
        self.cafe = cafe
        super().__init__()

    def run(self):
        self.cafe.serve_customer(self.number)


queue = queue.Queue()
# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
# print(tables)

cafe = Cafe(tables=tables)
# cafe.customer_arrival()
# print(cafe.serve_customer())
# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
