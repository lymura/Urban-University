from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

# Ваш токен API
api = '7807279654:AAFy1xZ_WK4RtT8IqQm_s_B-yDDsJdSkqYQ'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

# Группы состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

# Функции для обработки состояний

# set_age
@dp.message_handler(text="Calories")
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


# Состояние возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)

    await message.answer("Введите свой рост (в см):")
    await UserState.next()  # Переход к следующему состоянию (ожидание роста)

# Состояние роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['growth'] = float(message.text)

    await message.answer("Введите свой вес (в кг):")
    await UserState.next()  # Переход к следующему состоянию (ожидание веса)

# Состояние веса
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['weight'] = float(message.text)

    # Получим все данные из состояния
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    # Формула Миффлина - Сан Жеора для мужчин
    calories_norm = 10 * weight + 6.25 * growth - 5 * age + 5

    answer_text = f"Норма калорий для вас составляет примерно {calories_norm:.0f} ккал."
    await message.answer(answer_text)

    # Завершение машины состояний
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)