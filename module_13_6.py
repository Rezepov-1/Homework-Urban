from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Рассчитать')
kb.row(button, button2)

inline_kb = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(button_calories, button_formulas)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью", reply_markup=kb)

@dp.message_handler(text="Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_text = (
        "Формула Миффлина-Сан Жеора:\n"
        "10 x вес (кг) + 6.25 x рост (см) - 5 x возраст (г) + 5"
    )
    await call.message.answer(formula_text)
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст")
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост в см.')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    set_weight = float(data['weight'])
    set_growth = float(data['growth'])
    set_age = float(data['age'])

    calories = (10 * set_weight) + (6.25 * set_growth) - (5 * set_age) + 5
    await message.answer(f"Ваша норма калорий в сутки составляет: {calories}")
    await state.finish()


@dp.message_handler(state=None)
async def all_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)