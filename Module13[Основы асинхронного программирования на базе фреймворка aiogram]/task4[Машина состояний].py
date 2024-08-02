from Config.token import TG_TOKEN  # Импорт токена бота
from aiogram import (Bot,  # Импорт класса Bot для взаимодействия с Telegram API
                     Dispatcher,
                     F,  # Импорт F для фильтров
                     Router)  # Импорт Router для маршрутизации сообщений
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext  # Импорт контекста для работы с состояниями
from aiogram.fsm.state import State, StatesGroup  # Импорт классов для работы с состояниями

from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
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


async def set_id(state: FSMContext, message: Message, bob_mess: Message = None) -> None:
    """
    Функция для сохранения идентификаторов сообщений
    """
    data = await state.get_data()  # Получение данных из состояния
    mess = list(data.get('bot_mess', []))  # Получаем список сообщений или создаём пустой
    # Собираем id сообщений для удаления
    if bob_mess is not None:
        mess.append({'chat_id': bob_mess.chat.id, 'message_id': bob_mess.message_id})
        # print('add', bob_mess.text)
    mess.append({'chat_id': message.chat.id, 'message_id': message.message_id})
    # print('add', message.text)
    # Фи-и
    # mess += [{'chat_id': message.chat.id,
    #           'message_id': message.message_id}] + ([{'chat_id': bob_mess.chat.id,
    #                                                   'message_id': bob_mess.message_id}] if bob_mess else [])
    # Обновляем список сообщений
    await state.update_data(bot_mess=mess)  # Обновляем список сообщений в состоянии


async def delete_messages(state: FSMContext) -> None:
    """
    Функция для удаления сообщений бота из чата
    """
    data = await state.get_data()  # Получение данных из состояния
    messages = [mess for mess in data["bot_mess"]]
    # print('link', messages)
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
    await state.set_state(None)  # Обнуляем состояние
    await state.update_data(name=message.from_user.full_name)  # Сохраняем имя пользователя
    # Отправляем сообщение с командами
    bot_mess = await message.answer(f"Команды:\n"
                                    f"Calories- расчета калорий для оптимального похудения или "
                                    f"сохранения нормального веса",
                                    reply_markup=ReplyKeyboardRemove())
    await set_id(state, bot_mess)  # Сохраняем идентификатор сообщения


@router.message(UserStates.gender)
async def set_gender(message: Message, state: FSMContext) -> None:
    """
    Обработчик для установки пола пользователя
    """
    if message.text.lower() not in ["м", "ж"]:
        bot_mess = await message.answer(f"Введите правильный пол!")
        await set_id(state, message, bot_mess)
        return
    await set_id(state, message)
    await delete_messages(state)

    await state.update_data(gender=message.text)
    await state.set_state(UserStates.age)
    bot_mess = await message.answer("Какой Ваш возраст?",
                                    reply_markup=ReplyKeyboardRemove(),
                                    )
    await set_id(state, bot_mess)


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
async def process_unknown_write(message: Message) -> None:
    await message.reply("Что то пошло не так!",
                        reply_markup=ReplyKeyboardRemove())
    await message.answer(
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


@router.message()
async def cmd_all(message: Message, state: FSMContext) -> None:
    if message.text.lower().strip() == "calories":
        await state.update_data(name=message.from_user.full_name)
        await state.set_state(UserStates.gender)
        bot_mess = await message.answer(f"Какой Ваш пол: М или Ж ?",
                                        reply_markup=ReplyKeyboardRemove())
        await set_id(state, message, bot_mess)
    elif UserStates:
        bot_mess = await message.answer("Начните с команды /start",
                                        reply_markup=ReplyKeyboardRemove())
        await set_id(state, message, bot_mess)


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

# **Задача "Цепочка вопросов"**
# 1. Импортируйте классы `State` и `StateGroup` из `aiogram.dispatcher.filters.state`.
# 2. Создайте класс `UserState`, наследуемый от `StateGroup` с тремя состояниями: `age`, `growth`, `weight`.
#
# **Функции для обработки состояний:**
# 1. `set_age(message)`:
#     - Оберните в `message_handler`, реагирующий на текст 'Calories'.
#     - Выводит сообщение 'Введите свой возраст:'.
#     - Ожидает ввода возраста и устанавливает его в `UserState.age`.
# 2. `set_growth(message, state)`:
#     - Оберните в `message_handler`, реагирующий на состояние `UserState.age`.
#     - Обновляет состояние `age` на `message.text`.
#     - Выводит сообщение 'Введите свой рост:'.
#     - Ожидает ввода роста и устанавливает его в `UserState.growth`.
# 3. `set_weight(message, state)`:
#     - Оберните в `message_handler`, реагирующий на состояние `UserState.growth`.
#     - Обновляет состояние `growth` на `message.text`.
#     - Выводит сообщение 'Введите свой вес:'.
#     - Ожидает ввода веса и устанавливает его в `UserState.weight`.
# 4. `send_calories(message, state)`:
#     - Оберните в `message_handler`, реагирующий на состояние `UserState.weight`.
#     - Обновляет состояние `weight` на `message.text`.
#     - Сохраняет все данные из состояний в переменную `data`.
#     - Использует формулу Миффлина-Сан Жеора для расчета калорий.
#     - Отправляет результат пользователю.
#     - Завершает машину состояний методом `finish()`.
# **Примечание:** Все функции и методы должны быть асинхронными и запускаться с `await`.
