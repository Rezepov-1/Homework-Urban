from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = " "
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())

# @dp.message_handler()
# async def all_message(message):
#    print("Введите команду /start, чтобы начать общение.")
#    await message.answer("Введите команду /start, чтобы начать общение.")
#
# @dp.message_handler(commands=['start'])
# async def start_message(message):
#     print('Привет! Я бот помогающий твоему здоровью.')
#     await message.answer("Привет! Я бот помогающий твоему здоровью.")
#

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = "Калории")
async def set_age(message):
    await message.answer("Введите свой возраст")
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age= message.text)
    await message.answer('Введите свой рост, в см.')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth= message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight= message.text)
    data = await state.get_data()
    set_weight = float(data['weight'])
    set_growth = float(data['growth'])
    set_age = float(data['age'])

    calories = (10 * set_weight) + (6.25 * set_growth) - (5 * set_age) + 5
    await message.answer(f"Ваша норма калорий в сутки, составляет: {calories}")
    #полученные данные в data можно записывать себе куда-то в лог или еще куда
    await state.finish()

#для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
#для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.

# @dp.message_handler(commands=['start'])
# async def start_message(message):
#     print('Привет! Я бот помогающий твоему здоровью.')
#
# @dp.message_handler()
# async def all_message(message):
#    print("Введите команду /start, чтобы начать общение.")
#
#



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)
