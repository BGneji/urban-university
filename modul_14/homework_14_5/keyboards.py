from  aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton


"""ReplyKeyboardMarkup"""
# инициализация клавиатуры resize_keyboard=True подстраивает клавиатуру под интерфейс
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')

# добавляет кнопку по строчно
kb.add(button, button2)

kb.add(button3, button4)


"""InlineKeyboardMarkup"""
kb1 = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb1.add(button, button2)

product_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')],
    ]
)