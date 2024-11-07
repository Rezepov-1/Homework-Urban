from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
from crud_functions import initiate_db, get_all_products

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Инициализация базы данных и продуктов
initiate_db()
products = get_all_products()

# Проверка наличия записей в таблице и добавление продуктов, если таблица пустая
if not products:
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()
    sample_products = [
        ("Product1", "Описание 1", 100),
        ("Product2", "Описание 2", 200),
        ("Product3", "Описание 3", 300),
        ("Product4", "Описание 4", 400),
    ]
    cursor.executemany("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", sample_products)
    conn.commit()
    conn.close()
    products = get_all_products()

# Ссылки на изображения для продуктов загруженные мной на imgur
product_images = [
    "https://i.imgur.com/IFvW9FA.jpeg",
    "https://i.imgur.com/MAcVOrQ.jpeg",
    "https://i.imgur.com/3o7pCL2.jpeg",
    "https://i.imgur.com/D0woV2N.jpeg"
]

# Основная клавиатура с кнопками
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text='Информация'), KeyboardButton(text='Рассчитать'), KeyboardButton(text='Купить'))

# Inline клавиатура для продуктов
inline_product_kb = InlineKeyboardMarkup(row_width=1)
inline_product_kb.add(
    InlineKeyboardButton(text="Product1", callback_data="product_buying"),
    InlineKeyboardButton(text="Product2", callback_data="product_buying"),
    InlineKeyboardButton(text="Product3", callback_data="product_buying"),
    InlineKeyboardButton(text="Product4", callback_data="product_buying"),
)

inline_kb = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(button_calories, button_formulas)

# Состояния пользователя для расчета калорий
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=kb)

# Обработчик кнопки "Купить"
@dp.message_handler(text="Купить")
async def get_buying_list(message: types.Message):
    products = get_all_products()
    for index, product in enumerate(products):
        title, description, price = product[1], product[2], product[3]
        await message.answer_photo(
            photo=product_images[index % len(product_images)],  # Осуществляем циклический доступ к картинкам
            caption=f"Название: {title} | Описание: {description} | Цена: {price}"
        )
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_product_kb)

# Обработчик покупки продукта
@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()
#Обработчик опции на выбор
@dp.message_handler(text="Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)

#Обработчик демонстрации формулы расчета
@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_text = (
        "Формула Миффлина-Сан Жеора:\n"
        "10 x вес (кг) + 6.25 x рост (см) - 5 x возраст (г) + 5"
    )
    await call.message.answer(formula_text)
    await call.answer()

# Обработчик для Inline-кнопки "Рассчитать норму калорий"
@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст")
    await UserState.age.set()
    await call.answer()

# Обработчики состояний для расчета калорий
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

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)