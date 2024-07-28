from aiogram.utils.keyboard import InlineKeyboardBuilder

from Config.token import TG_TOKEN  # Импорт токена бота
from aiogram import (Bot,  # Импорт класса Bot для взаимодействия с Telegram API
                     Dispatcher,
                     F,  # Импорт F для фильтров
                     Router, types)  # Импорт Router для маршрутизации сообщений
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext  # Импорт контекста для работы с состояниями
from aiogram.fsm.state import State, StatesGroup  # Импорт классов для работы с состояниями
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove, InlineKeyboardButton,
)
import asyncio

bot = Bot(token=TG_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
router = Router()  # Создание маршрутизатора для обработки сообщений


# Определение класса состояний пользователя
class UserStates(StatesGroup):  # Создание состояний
    name = State()  # Имя
    gender = State()  # Пол
    age = State()  # Возраст
    growth = State()  # Рост
    weight = State()  # Вес
    result = State()  # Результат
    bot_mess = State()  # Состояние для хранения сообщений бота


# Функция для сбора ссылок сообщений бота
async def set_id(state: FSMContext, message: Message, bob_mess: Message = None) -> None:
    """
    Функция для сохранения идентификаторов сообщений
    """
    data = await state.get_data()  # Получение данных из состояния
    mess = list(data.get('bot_mess', []))  # Получаем список сообщений или создаём пустой
    # Собираем id сообщений для удаления
    if bob_mess is not None:
        mess.append({'chat_id': bob_mess.chat.id, 'message_id': bob_mess.message_id})
    mess.append({'chat_id': message.chat.id, 'message_id': message.message_id})
    await state.update_data(bot_mess=mess)  # Обновляем список сообщений в состоянии


# Функция для удаления сообщений бота из чата
async def delete_messages(state: FSMContext) -> None:
    """
    Функция для удаления сообщений бота из чата
    """
    data = await state.get_data()  # Получение данных из состояния
    messages = [mess for mess in data["bot_mess"]]
    for msg in messages:  # Проходим по каждому сообщению
        try:
            await bot.delete_message(chat_id=msg['chat_id'], message_id=msg['message_id'])  # Удаляем сообщение из чата
        except Exception as e:
            print(f"Ошибка при удалении сообщения: {e}")
    await state.update_data(data["bot_mess"].clear())  # Обновляем данные


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    """
    Обработчик команды /start
    """
    await state.set_state(None)
    await state.update_data(name=message.from_user.full_name)  # Сохраняем имя пользователя
    btn = [[InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calc'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]]
    kb = InlineKeyboardBuilder(btn)
    bot_mess = await message.answer(
        f"Привет, {message.from_user.full_name}!", reply_markup=kb.as_markup())
    await set_id(state, message, bot_mess)


@router.callback_query(F.data == "formulas")
async def info(call: types.CallbackQuery, state: FSMContext) -> None:
    """
    Обработчик для кнопки "Информация"
    """
    bot_mess = await call.message.answer("Формула Миффлина-Сан Жеора:\n"
                                         "Мужчины: 10 × вес(кг) + 6.25 × рост(см) - 5 × возраст(лет) + 5\n"
                                         "Женщины: 10 × вес(кг) + 6.25 × рост(см) - 5 × возраст(лет) - 161")
    await set_id(state, bot_mess)
    await call.answer()


@router.callback_query(F.data == "calc")
async def info(call: types.CallbackQuery, state: FSMContext) -> None:
    """
    Обработчик для кнопки сбора информации о пользователе
    """
    await delete_messages(state)
    btn = [[InlineKeyboardButton(text='Мужской', callback_data='male'),
            InlineKeyboardButton(text='Женский', callback_data='female')]]
    kb = InlineKeyboardBuilder(btn)
    bot_mess = await call.message.answer("Какой Ваш пол?", reply_markup=kb.as_markup())
    await state.set_state(UserStates.age)
    await set_id(state, bot_mess)
    await call.answer()


@router.callback_query(F.data == "male")
async def male_gender(call: types.CallbackQuery, state: FSMContext) -> None:
    """
    Обработчик для кнопки "Мужской"
    """
    await delete_messages(state)
    bot_mess = await call.message.answer("Какой Ваш возраст?")
    await call.answer()
    await set_id(state, bot_mess)
    await state.update_data(gender='м')


@router.callback_query(F.data == "female")
async def female_gender(call: types.CallbackQuery, state: FSMContext) -> None:
    """
    Обработчик для кнопки "Женский"
    """
    await delete_messages(state)
    bot_mess = await call.message.answer("Какой Ваш возраст?")
    await call.answer()
    await set_id(state, bot_mess)
    await state.update_data(gender='ж')


@router.message(UserStates.age)
async def set_age(message: Message, state: FSMContext) -> None:
    """
    Обработчик для установки возраста
    """
    if not message.text.isdigit():
        bot_mess = await message.answer(f"Ошибка ввода!")
        await set_id(state, message, bot_mess)
        return
    await set_id(state, message)
    await delete_messages(state)

    await state.update_data(age=message.text)
    await state.set_state(UserStates.growth)
    bot_mess = await message.answer("Какой Ваш рост?",
                                    reply_markup=ReplyKeyboardRemove(),
                                    )
    await set_id(state, bot_mess)


@router.message(UserStates.growth)
async def set_growth(message: Message, state: FSMContext) -> None:
    """
    Обработчик для установки роста
    """
    if not message.text.isdigit():
        bot_mess = await message.answer(f"Ошибка ввода!")
        await set_id(state, message, bot_mess)
        return
    await set_id(state, message)
    await delete_messages(state)

    await state.update_data(growth=message.text)
    await state.set_state(UserStates.weight)
    bot_mess = await message.answer("Какой Ваш вес?",
                                    reply_markup=ReplyKeyboardRemove(),
                                    )
    await set_id(state, bot_mess)


@router.message(UserStates.weight)
async def set_weight(message: Message, state: FSMContext) -> None:
    """
    Обработчик для установки веса
    """
    if not message.text.isdigit():
        bot_mess = await message.answer(f"Ошибка ввода!")
        await set_id(state, message, bot_mess)
        return
    await set_id(state, message)
    await delete_messages(state)

    await state.update_data(weight=message.text)
    await state.set_state(UserStates.result)
    bot_mess = await message.answer(
        f"И так.\nхотите узнать результат?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Да"),
                    KeyboardButton(text="Нет"),
                ]
            ],
            resize_keyboard=True,
        ),
    )
    await set_id(state, bot_mess)


@router.message(UserStates.result, F.text.casefold() == "да")
async def select_yes(message: Message, state: FSMContext) -> None:
    await set_id(state, message)
    await delete_messages(state)  # Удаляем сообщения
    data = await state.get_data()
    await state.clear()  # Очищает данные состояния диалога

    name = data["name"]
    gender = data["gender"]
    age = data["age"]
    growth = data["growth"]
    weight = data["weight"]
    if gender == "м":
        bmr = (10 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5 * float(data['age'])) + 5
    else:
        bmr = (10 * float(data['weight'])) + (6.25 * float(data['growth'])) - (5 * float(data['age'])) - 161

    result_text = (
        f"{name}, согласно вашим данным:\n"
        f"```Параметры:\n"
        f"Пол: {gender.upper()}\n"
        f"Возраст: {age} лет\n"
        f"Рост: {growth} см\n"
        f"Вес: {weight} кг\n```"
    )
    result_text += f"\n*Отлично! Ваша норма калорий: {round(bmr, 3)} ккал*\nЧто бы продолжить введите /start"

    await message.answer(text=result_text, reply_markup=ReplyKeyboardRemove(), parse_mode="Markdown")


@router.message(UserStates.result, F.text.casefold() == "нет")
async def select_no(message: Message, state: FSMContext) -> None:
    await delete_messages(state)
    await state.clear()  # Очищает данные из состояний
    await message.reply("О-очень жаль :(\nЧто бы продолжить введите /start",
                        reply_markup=ReplyKeyboardRemove())


@router.message(UserStates.result)
async def process_unknown_write(message: Message, state: FSMContext) -> None:
    bot_mess = await message.reply("Что то пошло не так!",
                                  reply_markup=ReplyKeyboardRemove())
    await set_id(state, bot_mess)
    bot_mess = await message.answer(
        f"Хотите узнать результат?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Да"),
                    KeyboardButton(text="Нет"),
                ]
            ],
            resize_keyboard=True,
        ),
    )
    await set_id(state, message, bot_mess)


@router.message()
async def cmd_all(message: Message, state: FSMContext) -> None:
    if UserStates:
        bot_mess = await message.answer("Начните с команды /start",
                                        reply_markup=ReplyKeyboardRemove())
        await set_id(state, message, bot_mess)


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    # await bot.delete_webhook(drop_pending_updates=True)  # Пропускаем все накопленные входящие
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:

        asyncio.run(main())
    except KeyboardInterrupt:
        pass

# **Задача "Ещё больше выбора"**#
# 1. Создайте клавиатуру `InlineKeyboardMarkup` с двумя кнопками `InlineKeyboardButton`:
#     - Текст: 'Рассчитать норму калорий', `callback_data='calories'`
#     - Текст: 'Формулы расчёта', `callback_data='formulas'`#
# 2. Напишите функцию `main_menu(message)`:
#     - Оберните в `message_handler`, срабатывающий при тексте 'Рассчитать'.
#     - Присылает Inline меню и текст 'Выберите опцию:'.#
# 3. Напишите функцию `get_formulas(call)`:
#     - Оберните в `callback_query_handler`, реагирующий на `callback_data='formulas'`.
#     - Присылает сообщение с формулой Миффлина-Сан Жеора.#
# 4. Измените функцию `set_age` и её декоратор:
#     - Декоратор измените на `callback_query_handler`, реагирующий на `callback_data='calories'`.
#     - Функция принимает `call` вместо `message`. Доступ к сообщению через `call.message`.
#
# **Алгоритм работы:**#
# 1. Вводится команда `/start`.
# 2. Присылается меню с кнопками 'Рассчитать' и 'Информация'.
# 3. Нажатие на кнопку 'Рассчитать' присылает Inline меню с кнопками 'Рассчитать норму калорий' и 'Формулы расчёта'.
# 4. Нажатие на кнопку 'Формулы расчёта' присылает сообщение с формулой.
# 5. Нажатие на кнопку 'Рассчитать норму калорий' запускает машину состояний по цепочке.
