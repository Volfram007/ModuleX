from Config.token import TG_TOKEN  # Импорт токена бота
from crud_functions import *
import asyncio
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Dispatcher, Bot, Router, F, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardButton, URLInputFile, \
    InputMediaPhoto

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
    t_State = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    """
    Обработчик команды /start
    """
    await state.set_state(None)
    await message.answer(
        f"Привет, {message.from_user.full_name}\n"
        f"Жми список товаров",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Список товаров"),
                ],
            ],
            resize_keyboard=True,
        ),
    )


@router.message(F.text.casefold() == "список товаров")
async def set_products(message: Message) -> None:
    db = get_all_products()
    media = []  # Список изображений
    btn = []  # Список кнопок

    for product in db:
        title, description, price, link = product[1:]  # Извлекаем данные из таблицы
        media += [InputMediaPhoto(
            media=URLInputFile(link),
            caption=f'Название: `{title}`\n'
                    f'Описание: `{description}`\n'
                    f">Цена: {price}₽",
            parse_mode=ParseMode.MARKDOWN_V2
        )]
        btn += [[InlineKeyboardButton(text=f'{title} {price}₽', callback_data=f'buy{title}')]]  # Создаём кнопки

    await message.answer_media_group(media=media)  # Отправляем все фото в одном сообщении
    kb = InlineKeyboardBuilder(btn)
    await message.answer(
        f"Выберите товар для покупки", reply_markup=kb.as_markup())


@router.callback_query(F.data[0:3] == 'buy')
async def info(call: types.CallbackQuery) -> None:
    """
    Обработчик для кнопки "Покупка"
    """
    await call.message.answer(f'Поздравляю с покупкой: {call.data[3:]}')
    await call.answer()


@router.message()
async def cmd_all(message: Message, state: FSMContext) -> None:
    if UserStates:
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
        initiate_db()

        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        print("Бот остановлен")

# **Задача "Продуктовая база"**
# 1. **Подготовка:**
#    - Используйте код из предыдущей задачи.
#    - Дополните его, следуя нижеописанным пунктам.
# 2. **Создание файла `crud_functions.py`:**
#    - Напишите функции:
#      - `initiate_db`: создаёт таблицу `Products`, если она ещё не создана. Поля таблицы:
#        - `id` - целое число, первичный ключ
#        - `title` - текст (не пустой)
#        - `description` - текст
#        - `price` - целое число (не пустой)
#      - `get_all_products`: возвращает все записи из таблицы `Products`.
# 3. **Изменения в Telegram-боте:**
#    - В начале запускайте функцию `initiate_db`.
#    - Измените функцию `get_buying_list`, используя данные из `get_all_products` для вывода информации о продуктах:
#      - "Название: <title> | Описание: <description> | Цена: <price>"
# 4. **Наполнение базы:**
#    - Перед запуском бота добавьте 4 или более записей в таблицу `Products`.
#
# **Пример результата выполнения программы:**
# - Записи в таблице `Products` и их отображение в Telegram-боте.
# **Примечания:**
# - Название продуктов и картинки к ним можете выбрать самостоятельно (минимум 4).
