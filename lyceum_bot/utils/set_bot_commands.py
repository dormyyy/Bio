from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Вивести довідку"),
            types.BotCommand("work", "Розпочати роботу з ботом"),
            types.BotCommand("exit", "Вийти з системи"),
            types.BotCommand("finish", "Завершити сесію"),
        ]
    )
