from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery

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

# Inline Keyboard
inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

# Main menu function
@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)

# Get formulas function
@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора: BMR = 10 × вес + 6.25 × рост - 5 × возраст - 161")

# Update set_age function
@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: CallbackQuery):
    await call.message.answer("Введите свой возраст:")
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




# Создаем клавиатуру с двумя кнопками
#@dp.message_handler(text='Рассчитать')
async def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Рассчитать')
    button2 = KeyboardButton('Информация')
    keyboard.add(button1, button2)
    await message.answer('Выберите действие:', reply_markup=keyboard)

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

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)