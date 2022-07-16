import time
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import bot, dp, db
from aiogram.types import ContentTypes
from keyboards.default.default_keyboard import request_contact
from states import Steps


user = {}


@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
    user.update({"id": message.from_user.id})
    select = await db.select_table_user_id(user)
    try:
        if user["id"] == select[0]["id"]:
            await Steps.preworkState.set()
            await message.answer(f"""Радий знову вас бачити, {select[0]["surname"]} {select[0]["name"]}""")
            await message.answer("Для початку роботи з ботом: /work")
    except:
        date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(time.time()))
        date = date.split()
        date = date[4]
        date = date.split(":")
        date = date[0]
        if date == "00":
            date = 0
        date = int(date)
        if 6 <= date < 12:
            await message.answer("Доброго ранку!")
        elif 12 <= date < 18:
            await message.answer("Доброго дня!")
        elif 18 <= date <= 23:
            await message.answer("Доброго вечора!")
        else:
            await message.answer("Доброї ночі!")
        await Steps.nameState.set()
        await bot.send_message(message.from_user.id, "Введіть спочатку своє справжнє прізвище, а потім ім`я\
 для авторизації.")


@dp.message_handler(state=Steps.nameState)
async def bot_name(message: types.Message):
    try:
        name = message.text.split()[1]
        surname = message.text.split()[0]
        user.update({"name": name})
        user.update({"surname": surname})
        await message.answer(f"Дякую, {surname} {name}.")
        await Steps.phoneState.set()
        await bot.send_message(message.from_user.id, "Відправте свій контакт для завершення авторизації",
                               reply_markup=request_contact)
    except:
        await message.answer(f"Дані введені невірно.")


@dp.message_handler(content_types=ContentTypes.CONTACT, state=Steps.phoneState)
async def bot_phone(message: types.Message):
    if "+" in message.contact.phone_number:
        contact = message.contact.phone_number
    else:
        contact = "+" + message.contact.phone_number
    user.update({"contact": contact})
    await Steps.preworkState.set()
    await bot.send_message(message.from_user.id, f"Дякую за авторизацію. Для початку роботи з ботом: /work")
    await db.insert_table_user(user)
