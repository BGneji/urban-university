# ЦельЦель задания:
# Практически применить знания о механизмах блокировки потоков в Python, используя класс Lock из модуля threading.
#
# Задание:
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
#
# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки,
# чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.
import threading
from threading import Thread, Lock

lock = Lock()


class BankAccount(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 1000

    def deposit(self, value):
        # пока идет пополнение баланса в цикле снять деньги не получится
        with lock:
            self.balance += value
            print(f'Deposited {value}, new balance is {self.balance}')

    def withdraw(self, take):
        with lock:
            self.balance -= take
            print(f'Withdrew  {take}, new balance is {self.balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
