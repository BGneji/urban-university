import logging
from time import sleep
from crud_functions import *
from dotenv import load_dotenv
import os

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import *

load_dotenv()

api = os.getenv('API1')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    """State: age, growth, weight (возраст, рост, вес)."""
    age = State()
    growth = State()
    weight = State()
    gender = State()


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=kb1)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    text = 'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5'
    text1 = 'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161'
    await call.message.answer(f'{text} \n {text1}')
    await call.answer()


# @dp.callback_query_handler(text='calories')
# async def info_calories(call):
#     await call.message.answer('Информация об calories')
#     # обязательно делать это
#     await call.answer()


@dp.message_handler(commands=['start'])
async def start(message):
    text = 'Привет! Я бот помогающий твоему здоровью!'
    await message.answer(text, reply_markup=kb)


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await message.answer('Введите свой рост:')
    await state.update_data(age=message.text)
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await message.answer('Введите свой вес:')
    await state.update_data(growth=message.text)
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_weight(message, state):
    await message.answer('У кажите совой пол:')
    await state.update_data(weight=message.text)
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def send_calories(message, state):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    print(data)
    if data['gender'].lower() == 'м':
        age = 5 * int(data['age']) + 5
        growth = 6.25 * int(data['growth'])
        weight = 10 * int(data['weight'])
    elif data['gender'].lower() == 'ж':
        age = 5 * int(data['age']) - 161
        growth = 6.25 * int(data['growth'])
        weight = 10 * int(data['weight'])
    res = weight + growth - age
    print(res)
    await message.answer(f"Ваша норма калорий {res}")
    await state.finish()


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    all_product = get_all_products()
    for i in range(len(all_product)):
        text = f"Название: {all_product[i][1]} | {all_product[i][2]} | {all_product[i][3]}"
        with open('file/2.png', 'rb') as img:
            await message.answer_photo(img, text)
            sleep(0.5)
    sleep(1)
    await message.answer("Выберите опцию", reply_markup=product_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    text = 'Вы успешно приобрели продукт!'
    await call.message.answer(f'{text}')
    await call.answer()


@dp.message_handler(text=['Информация'])
async def info(message):
    text = 'Привет! Я бот помогающий твоему здоровью.'
    await message.answer(text)


@dp.message_handler()
async def all_massages(message):
    """Функция для обработки всех входящих сообщений"""
    text = 'Введите команду /start что бы начать общение'
    await message.answer(text)
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
