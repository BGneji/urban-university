import logging

from dotenv import load_dotenv
import os

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

load_dotenv()

load_dotenv()

api = os.getenv('API')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())



class UserState(StatesGroup):
    """State: age, growth, weight (возраст, рост, вес)."""
    age = State()
    growth = State()
    weight = State()
    gender = State()
@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
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


@dp.message_handler(commands=['start'])
async def start_message(message):
    text = 'Привет! Я бот помогающий твоему здоровью.'
    await message.answer(text)
    print(f'Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message):
    """Функция для обработки всех входящих сообщений"""
    text = 'Введите команду /start что бы начать общение'
    await message.answer(text)
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
