from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandExit
from aiogram.dispatcher.storage import FSMContext
from loader import bot, dp, db


@dp.message_handler(CommandExit(), state="*")
async def bot_exit(message: types.Message, state=FSMContext):
    user_id = message.from_user.id
    await db.delete_table_user_id(user_id)
    await bot.send_message(user_id, "Дякую за роботу, ви вийшли з системи!")
    await state.finish()
