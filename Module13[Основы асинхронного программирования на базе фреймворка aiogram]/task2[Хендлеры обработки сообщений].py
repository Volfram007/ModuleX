from aiogram import Bot, Dispatcher
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from Config.token import TG_TOKEN  # Импорт токена
import asyncio

router = Router()  # создание роутера


@router.message(CommandStart())  # обработчик команды /start
async def cmd_start(message: Message):
    print('Привет! Я бот помогающий твоему здоровью.')  # отправка сообщения в консоль


@router.message()  # обработчик остальных сообщений
async def cmd_chat(message: Message):
    print('Напишите команду /start, чтобы начать общение.')  # отправка сообщения в консоль


async def main():
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()  # создание диспетчера
    dp.include_router(router)  # Добавляет роутер в диспетчер
    await dp.start_polling(bot)  # Запуск диспетчера событий


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

# **Задача "Бот поддержки (Начало)"**
# 1. Напишите две асинхронные функции:
#     - `start(message)`:
#         - Печатает в консоли: 'Привет! Я бот, помогающий твоему здоровью.'
#         - Запускается при команде '/start' в чате с ботом (используйте соответствующий декоратор).
#     - `all_messages(message)`:
#         - Печатает в консоли: 'Введите команду /start, чтобы начать общение.'
#         - Запускается при любом другом обращении (используйте соответствующий декоратор).
# 2. Запустите Telegram-бота и проверьте его работу.
# **Пример ввода в чат Telegram:**
# ```
# Хэй!
# /start
# ```
# **Пример вывода в консоль:**
# ```
# Updates were skipped successfully.
# Введите команду /start, чтобы начать общение.
# Привет! Я бот, помогающий твоему здоровью.
# ```
