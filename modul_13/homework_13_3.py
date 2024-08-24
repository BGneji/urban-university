from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

load_dotenv()

api = os.getenv('API')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


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
