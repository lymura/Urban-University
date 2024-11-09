from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio

api = '7807279654:AAFy1xZ_WK4RtT8IqQm_s_B-yDDsJdSkqYQ'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

# Группы состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создаем клавиатуру с двумя кнопками
#@dp.message_handler(text='Рассчитать')
async def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Рассчитать')
    button2 = KeyboardButton('Информация')
    keyboard.add(button1, button2)
    await message.answer('Выберите действие:', reply_markup=keyboard)

    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    # Calculate calorie norm using the Mifflin - St Jeor formula
    # Example formula calculation for women:
    # BMR = 10 × weight + 6.25 × height - 5 × age - 161.

    bmr = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) - 161

    await message.answer(f"Your daily calorie norm is: {bmr}")

    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

