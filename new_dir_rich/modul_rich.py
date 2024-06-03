# pip install rich
import time
from rich import print
from rich.columns import Columns
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
console = Console()



from datetime import datetime

current_date = datetime.now().replace(microsecond=0)
formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')


store_adress = 'Адрес магазина: Тула, улица Фрунзе, дом 1'


# style = "bold 2"


def menu():
    console.print(Panel.fit('Выберите одну из операций!\n'
                            '\n '
                            '1. Добавить товар\n '
                            '2. Что в корзине\n '
                            '3. Очистить корзину\n '
                            '4. Создать чек \n '
                            '5. Завершить работу \n '
                            '6. Посмотреть меню ', title="Касса.py", style="color(5)"))
    # console.print("Выберите одну из операций!", style="color(3)")
    # print()
    # console.print("1. Добавить товар", style="color(5)")
    # console.print("2. Что в корзине", style="color(5)")
    # console.print("3. Очистить корзину", style="color(5)")
    # console.print("4. Создать чек", style="color(5)")
    # console.print("5. Завершить работу", style="color(5)")
    # console.print('6. Посмотреть меню', style="color(5)")
    # print()


menu()
'''Список с продуктами'''
product_dict = {'кофе': [1000, 2000], 'чай': [2000]}


def add_product():
    '''Добавляем продукт в корзину'''
    global product_dict
    product = input('Что хотите добавить в корзину? ')
    price = int(input('Уточните цену товара? '))
    product_dict[product] = product_dict.get(product, []) + [price]



def empty_cart():
    '''Очищаем корзину с продуктами'''
    global product_dict
    product_dict = {}


def cart():
    '''Корзина с продуктами'''
    table = Table()
    table.add_column("Дата покупки", justify="center", style="cyan", no_wrap=True)
    table.add_column("Наименования продукта", style="magenta")
    table.add_column("Количество", justify="right", style="green")
    table.add_column("Цена", justify="right", style="green")
    table.add_column("Итого", justify="right", style="green")
    for key, value in product_dict.items():
        quantity = len(product_dict[key])
        price = sum(value)/quantity
        total = sum(value)
        dubl_pa = Panel(Columns([key, str(total)]))
        console.print(dubl_pa)
        table.add_row(formatted_date, key, str(quantity), str(price), str(total))
    return console.print(Panel.fit(table, title="Корзина", style="color(5)"))


def check():
    '''Вывод чека'''
    def do_work():
        for i in range(1):
            print('')
            time.sleep(1)
        print()
    with console.status('Идет печать чека...', spinner='dots'):
        do_work()

    sum_quantity = 0
    sum_total = 0
    for key, value in product_dict.items():
        quantity = len(product_dict[key])
        total = sum(value)
        dubl_pa = Columns([key, value])
        sum_quantity += quantity
        sum_total += total

    console.print(Panel.fit(f'Большое спасибо за покупку!\n'
                            f'Будем ждать вас еще!\n'
                            f'___________________________\n'
                            f'Кол-во товаров: {sum_quantity}\n'
                            f'Общая стоимость: {sum_total}\n'
                            f'Продавец: Иванов Иван Иванович\n'
                            f'{store_adress}'.center(150), title="Чек"), justify='left')
    print('Чек готов!!!')



n = 0
while True:
    # n = int(input('Что хочешь сделать? (1-6) '))
    n = int(Prompt.ask('Что хочешь сделать? (1-6) ', choices=['1', '2', '3', '4', '5', '6'], default='6'))
    print()
    if n == 1:
        add_product()
    elif n == 2:
        cart()
        print(product_dict)
    elif n == 3:
        empty_cart()

        print('Корзина пуста')
    elif n == 4:
        check()

    elif n == 5:
        a = console.input('Вы действительно хотите выйти y/n ',)
        if a == 'y':
            break
        else:
            continue
    elif n == 6:
        menu()
    print('*' * 10)
    print('6. Посмотреть меню ')


