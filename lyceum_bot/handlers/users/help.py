from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Запустити бота",
            "/help - Отримати довідку",
            "/work - Почати роботу з ботом",
            "/exit - Вийти з системи",
            "/finish - Звершити сесію")
    
    await message.answer("\n".join(text))
