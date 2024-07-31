import asyncio

from aiogram.utils.keyboard import InlineKeyboardBuilder

from Config import db
from aiogram import Dispatcher, Bot, Router, F, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, FSInputFile, InlineKeyboardButton, URLInputFile
from Config.token import TG_TOKEN  # Импорт токена бота

bot = Bot(token=TG_TOKEN, )
router = Router()  # Создание маршрутизатора для обработки сообщений


class UserStates(StatesGroup):
    t_State = State()


# Функция для сбора ссылок сообщений бота
async def set_id(state: FSMContext, mess1: Message, mess2: Message = None) -> None:
    """
    Функция для сохранения идентификаторов сообщений
    """
    data = await state.get_data()  # Получение данных из состояния
    mess = list(data.get('bot_mess', []))  # Получаем список сообщений или создаём пустой
    # Собираем id сообщений для удаления
    if mess2 is not None:
        mess.append({'chat_id': mess2.chat.id, 'message_id': mess2.message_id})
    mess.append({'chat_id': mess1.chat.id, 'message_id': mess1.message_id})
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
    bot_mess = await message.answer(
        f"Привет, {message.from_user.full_name}\n"
        f"Я бот помогающий твоему здоровью",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Рассчитать"),
                    KeyboardButton(text="Информация"),
                ],
                [
                    KeyboardButton(text="Купить"),
                ],
            ],
            resize_keyboard=True,
        ),
    )
    await set_id(state, message, bot_mess)


@router.message(F.text.casefold() == "рассчитать")
async def buy(message: Message, state: FSMContext) -> None:
    bot_mess = await message.answer_photo(photo=URLInputFile(
        "https://prorisuem.ru/foto/9283/risunok_bolezniam_vkhod_vospreshchen_3_klass_44.webp"),
        caption=f'Конец кода [или когда мне влом копировать старый код]'
                f'(https://github.com/Volfram007/ModuleX/blob/master/Module13%5B'
                f'Основы%20асинхронного%20программирования%20на%20базе%20фреймворка%20aiogram%5D/'
                f'task6%5BИнлайн%20клавиатуры%5D.py) \U0001F92A',
        parse_mode=ParseMode.MARKDOWN_V2)
    await set_id(state, message, bot_mess)


@router.message(F.text.casefold() == "информация")
async def buy(message: Message, state: FSMContext) -> None:
    bot_mess = await message.answer_photo(photo=URLInputFile(
        "https://avatars.mds.yandex.net/i?id=ddf573ef874d511d2ecde47275ed2347_l-4780598-images-thumbs&n=13"),
        caption=db.info)
    await set_id(state, message, bot_mess)


@router.message(F.text.casefold() == "купить")
async def buy(message: Message, state: FSMContext) -> None:
    # Разделяем текст на строки и обрабатываем каждую строку
    for i, line in enumerate(db.product.split('\n'), start=1):
        # Разделяем строку на столбцы
        columns = line.split(' | ')
        if len(columns) == 4:
            # Извлекаем информацию о продукте
            name, info, price, file_name = columns
            # Отправляем сообщение с картинкой и текстом
            bot_mess = await message.answer_photo(photo=FSInputFile(f'Config/{file_name}.jpg'),
                                                  caption=f'>*Название:* {name}\n'
                                                          f'*Описание*: {info}\n'
                                                          f'*Цена*: {i* int(price)}',
                                                  has_spoiler=True,
                                                  parse_mode=ParseMode.MARKDOWN_V2)
            await set_id(state, bot_mess)
    btn = [[InlineKeyboardButton(text='Перген', callback_data='ok'),
            InlineKeyboardButton(text='Вмазь', callback_data='ok'),
            InlineKeyboardButton(text='СтопТусин', callback_data='ok'),
            InlineKeyboardButton(text='НормаПив', callback_data='ok')]]
    kb = InlineKeyboardBuilder(btn)
    bot_mess = await message.answer(
        f"Выберите продукт для покупки", reply_markup=kb.as_markup())
    await set_id(state, message, bot_mess)


@router.callback_query(F.data == "ok")
async def buy_ok(call: types.CallbackQuery, state: FSMContext) -> None:
    await delete_messages(state)  # Удаляем сообщения из чата
    bot_mess = await call.message.answer_photo(photo=URLInputFile(
        'https://www.'
        'funnyart.club/uploads/posts/2023-02/1675536842_www-funnyart-club-p-prikolnie-chaiki-shutki-46.jpg'),
        caption='Вы успешно приобрели продукт! /start или любая карякуля для перезапуска')
    await set_id(state, bot_mess)  # Обновляем ссылки
    await call.answer()


@router.message()
async def cmd_all(message: Message, state: FSMContext) -> None:
    if UserStates:
        # Если состояние не установлено, то создаём состояние "/start"
        await cmd_start(message, state)


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    # await bot.delete_webhook(drop_pending_updates=True)  # Пропускаем все накопленные входящие
    await dp.start_polling(bot)  # Запуск бота


if __name__ == "__main__":
    try:

        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        print("Импровизация завершена")

# **Задача "Витамины для всех"**
# 1. **Подготовка:**
#    - Используйте код Telegram-бота из последнего домашнего задания модуля 13.
#    - Сохраните код в файл `module_14_3.py`.
# 2. **Дополнение кода Telegram-бота:**
# 3. **Создание клавиатур:**
#    - Добавьте кнопку "Купить" в главную (обычную) клавиатуру меню.
#    - Создайте Inline клавиатуру из 4 кнопок: "Product1", "Product2", "Product3", "Product4".
#    У всех кнопок `callback_data="product_buying"`.
# 4. **Создание хэндлеров и функций:**
#    - Создайте message хэндлер, который реагирует на текст "Купить" и оборачивает функцию `get_buying_list(message)`.
#    - Функция `get_buying_list` должна:
#      - Выводить 4 сообщения с информацией о продуктах:
#      'Название: Product<number> | Описание: описание <number> | Цена: <number * 100>'.
#      - Выводить картинки к продуктам после каждого сообщения.
#      - Выводить Inline меню с надписью "Выберите продукт для покупки:".
#    - Создайте callback хэндлер, который реагирует на текст "product_buying" и оборачивает
#    функцию `send_confirm_message(call)`.
#    - Функция `send_confirm_message` должна присылать сообщение "Вы успешно приобрели продукт!".
#
# **Пример результата выполнения программы:**
# - Обновлённое главное меню.
# - Список товаров и меню покупки.
