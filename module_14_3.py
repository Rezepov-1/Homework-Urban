from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Создаем основную клавиатуру
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_info = KeyboardButton(text='Информация')
button_calculate = KeyboardButton(text='Рассчитать')
button_buy = KeyboardButton(text='Купить')
kb.row(button_info, button_calculate)
kb.row(button_buy)

# Создаем Inline-клавиатуру для выбора продукта
inline_buy_kb = InlineKeyboardMarkup(row_width=2)
for i in range(1, 5):
    inline_buy_kb.add(InlineKeyboardButton(text=f'Product{i}', callback_data='product_buying'))

# Inline-клавиатура для выбора расчета калорий
inline_kb = InlineKeyboardMarkup(row_width=1)
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(button_calories, button_formulas)

# Состояния пользователя
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=kb)

# Обработчик для кнопки "Рассчитать" из основной клавиатуры
@dp.message_handler(text="Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)

# Обработчик для кнопки "Купить" из основной клавиатуры
@dp.message_handler(text="Купить")
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        await message.answer_photo(
            photo=f'https://thumbs.dreamstime.com/z/%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB-%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2%D0%B8%D1%82%D0%B0%D0%BC%D0%B8%D0%BD%D0%BE%D0%B2-110319057.jpg?ct=jpeg{i}',  # Заглушка для изображения
            caption=f"Название: Product{i} | Описание: описание {i} | Цена: {i * 100}"
        )
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_buy_kb)

# Обработчик для Inline-кнопки "Формулы расчёта"
@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    formula_text = (
        "Формула Миффлина-Сан Жеора:\n\n"
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

# Обработчик для покупки продукта
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

# Обработчик всех сообщений (будет срабатывать только если нет активного состояния)
@dp.message_handler(state=None)
async def all_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)