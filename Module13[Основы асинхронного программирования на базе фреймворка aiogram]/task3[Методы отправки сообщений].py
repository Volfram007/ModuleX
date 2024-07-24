from aiogram import Bot, Dispatcher
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from Config.token import TG_TOKEN  # Импорт токена
import asyncio

router = Router()  # создание роутера


@router.message(CommandStart())  # обработчик команды /start
async def cmd_start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')  # отправка сообщения


@router.message()  # обработчик остальных сообщений
async def cmd_chat(message: Message):
    if message.text.lower() == 'Привет'.lower():
        await message.answer('Напишите команду /start, чтобы начать общение.')  # отправка сообщения
    else:
        await message.answer('Я не понимаю вас.')


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

# Задача "Он мне ответил!":
# Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись в чате телеграм.
