import logging
import sys
from os import getenv
from typing import Any, Dict
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from Config.token import TG_TOKEN  # Импорт токена
import asyncio

TOKEN = TG_TOKEN
router = Router()


class UserStates(StatesGroup):  # Создание состояний
    name = State()  # Имя
    gender = State()  # Пол
    age = State()  # Возраст
    growth = State()  # Рост
    weight = State()  # Вес
    result = State()  # Результат


async def delete_messages(bot: Bot, messages: list):
    for msg in messages:
        await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.from_user.full_name)
    await state.set_state(UserStates.gender)
    await message.answer(f"Какой Ваш пол: М или Ж ?",
                         reply_markup=ReplyKeyboardRemove())


@router.message(UserStates.gender)
async def chat(message: Message, state: FSMContext) -> None:
    if message.text.lower() not in ["м", "ж"]:
        data = await state.get_data()
        await message.answer(f"Введите правильный пол!")
        return

    await state.update_data(gender=message.text)
    await state.set_state(UserStates.age)
    await message.answer("Какой Ваш возраст?",
                         reply_markup=ReplyKeyboardRemove(),
                         )


@router.message(UserStates.age)
async def chat(message: Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await state.set_state(UserStates.growth)
    await message.answer("Какой Ваш рост?",
                         reply_markup=ReplyKeyboardRemove(),
                         )


@router.message(UserStates.growth)
async def chat(message: Message, state: FSMContext) -> None:
    await state.update_data(growth=message.text)
    await state.set_state(UserStates.weight)
    await message.answer("Какой Ваш вес?",
                         reply_markup=ReplyKeyboardRemove(),
                         )


@router.message(UserStates.weight)
async def chat(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    await state.set_state(UserStates.result)
    await message.answer(
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


@router.message(UserStates.result, F.text.casefold() == "да")
async def process_yes(message: Message, state: FSMContext) -> None:
    data = await state.update_data(result=message.text)
    await state.clear()  # Очищает данные из состояний

    name = data["name"]
    gender = data["gender"]
    age = data["age"]
    growth = data["growth"]
    weight = data["weight"]
    if gender == "м":
        bmr = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
    else:
        bmr = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) - 161

    result_text = (
        f"{name}, согласно вашим данным:\n"
        f"```Параметры:\n"
        f"**Пол**: {gender.upper()}\n"
        f"**Возраст**: {age} лет\n"
        f"**Рост**: {growth} см\n"
        f"**Вес**: {weight} кг\n```"
    )
    result_text += f"\n*Отлично! Вот ваш результат: {round(bmr, 3)} ккал*"

    await message.answer(text=result_text, reply_markup=ReplyKeyboardRemove(), parse_mode="Markdown")


@router.message(UserStates.result, F.text.casefold() == "нет")
async def process_no(message: Message, state: FSMContext) -> None:
    data = await state.get_data()  # Получаем данные из состояний
    await state.clear()  # Очищает данные из состояний
    await message.answer("О-очень жаль :(\nЧто бы продолжить введите /start",
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


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()  # создание диспетчера
    dp.include_router(router)  # Добавляет роутер в диспетчер
    await dp.start_polling(bot)  # Запуск диспетчера событий


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
