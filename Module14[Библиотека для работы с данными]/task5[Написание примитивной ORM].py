from Config.token import TG_TOKEN  # Импорт токена бота
from crud_functions import *
import re
import asyncio
import logging as log
from aiogram.enums import ParseMode
from aiogram import Dispatcher, Bot, Router, F, types
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardButton, URLInputFile, \
    ReplyKeyboardRemove, InputMediaPhoto

print("Запуск бота...", end='')
log.basicConfig(filename="py_log.log",
                level=log.WARNING,  # INFO WARNING ERROR CRITICAL
                filemode="w",
                encoding='utf-8',
                format="%(asctime)s %(levelname)s [%(module)s - %(funcName)s]  %(lineno)d - %(message)s",
                datefmt='%H:%M:%S')
bot = Bot(token=TG_TOKEN)
# Создание маршрутизатора для обработки сообщений
router = Router()


class UserStates(StatesGroup):
    StateRegister = State()
    StateLogin = State()
    StateMail = State()
    StateAge = State()
    bot_mess = State()


# Функция для сбора ссылок сообщений бота
async def set_id(state: FSMContext, message: Message, bob_mess: Message = None) -> None:
    """
    Функция для сохранения идентификаторов сообщений
    """
    data = await state.get_data()  # Получение данных из состояния
    mess = list(data.get('bot_mess', []))  # Получаем список ссылок или создаём пустой
    # Собираем id сообщений для удаления
    if bob_mess is not None:  # Если передан bob_mess, то добавляем ссылку в список
        mess.append({'chat_id': bob_mess.chat.id, 'message_id': bob_mess.message_id})
    mess.append({'chat_id': message.chat.id, 'message_id': message.message_id})  # Добавляем ссылку в список
    await state.update_data(bot_mess=mess)  # Обновляем список ссылок в состоянии


# Функция для удаления сообщений бота из чата
async def delete_messages(state: FSMContext) -> None:
    """
    Функция для удаления сообщений бота из чата
    """
    data = await state.get_data()  # Получение данных из состояния
    messages = [mess for mess in data["bot_mess"]]
    if len(messages) > 0:  # Если есть сообщения, то удаляем их
        for msg in messages:  # Проходим по каждому сообщению
            try:
                await bot.delete_message(chat_id=msg['chat_id'],
                                         message_id=msg['message_id'])  # Удаляем сообщение из чата
            except Exception as e:
                print(f"Ошибка при удалении сообщения: {e}")
        await state.update_data(data["bot_mess"].clear())  # Обновляем данные / очищаем список ссылок


async def bot_mess(text: str, *buttons, message: Message, state: FSMContext) -> None:
    """
    Функция для отправки сообщений бота
    """
    if buttons[0] is not None:  # Если есть кнопки, то отправляем сообщение с кнопками
        # Собираем кнопки
        kb = [[KeyboardButton(text=btn) for btn in b_list] for b_list in buttons]
        # Отправляем сообщение с кнопками
        id_mess = await message.answer(text=text,
                                       reply_markup=ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True))
    else:
        # Отправляем сообщение без кнопок
        id_mess = await message.answer(text, reply_markup=ReplyKeyboardRemove())
    await set_id(state, message, id_mess)


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    """
    Обработчик команды /start
    """
    await state.set_state(None)  # Обновляем состояние
    if is_included(message.from_user.id):
        # Если пользователь зарегистрирован, то переходим в режим авторизирован
        await state.update_data(StateRegister=message.from_user.id)
        # Выводим кнопки
        await bot_mess('Выберите "Список товаров"',
                       ['Список товаров'],
                       ['Удалить акк', 'Баланс'], message=message, state=state)
    else:
        # Если пользователь не зарегистрирован, то переходим в режим регистрации
        await bot_mess('Вы еще не зарегистрированы в системе',
                       ['Регистрация'], message=message, state=state)


@router.message(UserStates.StateRegister)
async def reg_user(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    # Обрабатываем ввод данных пользователя
    if 'StateLogin' not in data:
        # Проверка на корректность логина
        if not re.match(r"^[a-zA-Z0-9а-яА-Я_-]+$", message.text.strip()):
            await bot_mess('Спец символы запрещены', None, message=message, state=state)
            return
        elif is_validlogin(message.text.strip()):
            await bot_mess('Этот логин занят', None, message=message, state=state)
            return
        elif message.text.strip() == '':
            await bot_mess('Логин не может быть пустым', None, message=message, state=state)
            return
        await state.update_data(StateLogin=message.text.strip())
        await bot_mess('Введите почту', None, message=message, state=state)
    elif 'StateMail' not in data:
        if is_validlogin(message.text.strip()):
            await bot_mess('Эта почта занята', None, message=message, state=state)
            return
        # Проверка на корректность почты
        # if not re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", message.text.strip()):
        #     await bot_mess('Адрес почты не корректен', None, message=message, state=state)
        #     return
        await state.update_data(StateMail=message.text.strip())
        await bot_mess('Введите возраст', None, message=message, state=state)
    elif 'StateAge' not in data:
        if not message.text.strip().isdigit():
            await bot_mess('Введите возраст в числовом виде', None, message=message, state=state)
            return
        await state.update_data(StateAge=message.text.strip())
        data = await state.get_data()
        if not add_user(message.from_user.id,
                        data["StateLogin"],
                        data["StateMail"],
                        data["StateAge"],
                        ):
            print("Ошибка при добавлении пользователя")
        await cmd_start(message, state)


@router.message(F.text.casefold() == 'регистрация')
async def new_user(message: Message, state: FSMContext) -> None:
    if is_included(message.from_user.id):
        # Если такой пользователь уже есть в базе, отправляем команду /start.
        await cmd_start(message, state)
    else:
        # Если пользователь не зарегистрирован
        await bot_mess('Введите логин', None, message=message, state=state)
        await state.set_state(UserStates.StateRegister)


@router.message(F.text.casefold() == "баланс")
async def inf_user(message: Message, state: FSMContext) -> None:
    if is_included(message.from_user.id):
        res = info_user(message.text.strip().lower(), message.from_user.id)
        await bot_mess(f'Ваш баланс: {res} ₽',
                       ['Список товаров'],
                       ['Удалить акк', 'Баланс'], message=message, state=state)
    else:
        # Если пользователь не зарегистрирован
        await cmd_start(message, state)


@router.message(F.text.casefold() == "удалить акк")
async def exit_db(message: Message, state: FSMContext) -> None:
    await set_id(state, message)
    if is_included(message.from_user.id):
        await delete_messages(state)
        del_user(message.from_user.id)
    await state.clear()
    await cmd_start(message, state)


@router.message(F.text.casefold() == "список товаров")
async def set_products(message: Message, state: FSMContext) -> None:
    db = get_all_products()
    media = []  # Список изображений
    btn = []  # Список кнопок

    for product in db:
        title, description, price, link = product[1:]  # Извлекаем данные из таблицы
        # Заполняем массив изображений
        media += [InputMediaPhoto(
            media=URLInputFile(link),
            caption=f'Название: `{title}`\n'
                    f'Описание: `{description}`\n'
                    f">Цена: {price}₽",
            parse_mode=ParseMode.MARKDOWN_V2
        )]
        # Создаём кнопки
        btn += [[InlineKeyboardButton(text=f'{title} {price}₽', callback_data=f'buy{title}')]]
    # id_mess - получает массив ссылок на изображения
    id_mess = await message.answer_media_group(media=media)  # Отправляем все фото в одном сообщении
    kb = InlineKeyboardBuilder(btn)
    id_mess += [await message.answer(
        f"Выберите товар для покупки", reply_markup=kb.as_markup())]
    id_mess += [message]
    # Перебором отправляем ссылки
    [await set_id(state, i) for i in id_mess]


@router.callback_query(F.data[0:3] == 'buy')
async def info(call: types.CallbackQuery, state: FSMContext) -> None:
    """
    Обработчик для кнопки "Покупка"
    """
    data = await state.get_data()
    if 'StateRegister' not in data:
        # Если состояние не установлено, то создаём состояние "/start"
        await bot_mess(f'Начните с команды /start', None, message=call.message, state=state)
        await call.answer()
        return
    if buy_product(data["StateRegister"], call.data[3:]):
        id_mess = await call.message.answer(f'Поздравляю с покупкой: {call.data[3:]}')
    else:
        id_mess = await call.message.answer(f'Недостаточно средств на счёте')
    await set_id(state, id_mess)
    await call.answer()


@router.message()
async def cmd_all(message: Message, state: FSMContext) -> None:
    # Если состояние не установлено, то создаём состояние "/start"
    await cmd_start(message, state)


async def main():
    dp = Dispatcher()
    dp.include_router(router)  # Подключение маршрутизатора
    # Пропускаем все накопленные входящие
    # await bot.delete_webhook(drop_pending_updates=True)
    print(" OK")
    await dp.start_polling(bot)  # Запуск бота


if __name__ == "__main__":
    try:
        initiate_db()  # Инициализация базы данных
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

# **Задача "Регистрация покупателей"**
# **Подготовка:**
# - Используйте код из предыдущей задачи и дополните его.
#
# **Дополните файл `crud_functions.py`:**
# 1. **Функция `initiate_db`**:
#    - Дополните созданием таблицы `Users`, если она ещё не создана. Поля таблицы:
#      - `id` - целое число, первичный ключ
#      - `username` - текст (не пустой)
#      - `email` - текст (не пустой)
#      - `age` - целое число (не пустой)
#      - `balance` - целое число (не пустой)
# 2. **Функция `add_user(username, email, age)`**:
#    - Добавляет в таблицу `Users` запись с переданными данными.
#    - Баланс у новых пользователей равен 1000.
# 3. **Функция `is_included(username)`**:
#    - Принимает имя пользователя и возвращает `True`, если такой пользователь есть в таблице `Users`, иначе `False`.
#
# **Изменения в Telegram-боте:**
# 1. **Кнопки главного меню**:
#    - Дополните кнопкой "Регистрация".
# 2. **Новый класс состояний `RegistrationState`**:
#    - Объекты класса `State`: `username`, `email`, `age`, `balance` (по умолчанию 1000).
# 3. **Цепочка изменений состояний `RegistrationState`**:
#    - **Функция `sing_up(message)`**:
#      - Обёрнута в `message_handler`, реагирующий на текст "Регистрация".
#      - Выводит сообщение "Введите имя пользователя (только латинский алфавит):".
#      - Ожидает ввода для `RegistrationState.username`.
#    - **Функция `set_username(message, state)`**:
#      - Обёрнута в `message_handler`, реагирующий на состояние `RegistrationState.username`.
#      - Если пользователя `message.text` нет в таблице, обновляет состояние `username` на `message.text`.
#      - Выводит сообщение "Введите свой email:" и ожидает ввода для `RegistrationState.email`.
#      - Если пользователь существует, выводит "Пользователь существует, введите другое имя" и запрашивает новое
#      состояние для `RegistrationState.username`.
#    - **Функция `set_email(message, state)`**:
#      - Обёрнута в `message_handler`, реагирующий на состояние `RegistrationState.email`.
#      - Обновляет состояние `RegistrationState.email` на `message.text`.
#      - Выводит сообщение "Введите свой возраст:" и ожидает ввода для `RegistrationState.age`.
#    - **Функция `set_age(message, state)`**:
#      - Обёрнута в `message_handler`, реагирующий на состояние `RegistrationState.age`.
#      - Обновляет состояние `RegistrationState.age` на `message.text`.
#      - Берёт все данные (username, email, age) из состояния и записывает их в таблицу `Users`
#      с помощью функции `add_user`.
#      - Завершает приём состояний методом `finish()`.
#
# **Перед запуском бота:**
# - Пополните таблицу `Products` 4 или более записями для вывода в чате Telegram-бота.
