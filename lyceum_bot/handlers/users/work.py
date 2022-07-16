from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters.builtin import CommandFinish, CommandWork
from keyboards.default import main_keyboard
from keyboards.inline.inline_keyboards import place, subjects1, subjects2
import data
from loader import bot, dp, db
from aiogram.types import ContentTypes
from states import Steps


pull = {}
user = {}


@dp.message_handler(content_types=ContentTypes.ANY, state=None)
async def bot_work_0(message: types.Message):
    await message.answer("Для того, щоб розпочати роботу з ботом, потрібно авторизуватися: /start")


@dp.message_handler(CommandFinish(), state=Steps.workState)
async def bot_finish(message: types.Message, state=FSMContext):
    await message.answer("Сессія завершена")
    await state.finish()
    print(await state.get_state())


@dp.message_handler(CommandWork(), state=Steps.preworkState)
async def bot_work_1(message: types.Message):
    await Steps.workState.set()
    user.update({"id": message.from_user.id})
    await message.answer("Вас вітає телеграмм-бот Подільського ліцею. Для отримання інформації користуйтесь\
 клавіатурами", reply_markup=main_keyboard)


@dp.message_handler(text="Головна", state=Steps.workState)
async def bot_main(message: types.Message):
    await bot.send_message(message.from_user.id, "Секунду...")
    photo = open('data\materials\pntl_1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo)
    await bot.send_message(message.from_user.id, "https://pntl.edu.vn.ua/index.php/home")


@dp.message_handler(text="Розклад дзвінків", state=Steps.workState)
async def bot_rings(message: types.Message):
    tt = f"""
1 урок: 8:00 - 8:45
2 урок: 8:55 - 9:40
3 урок: 9:50 - 10:35
4 урок: 10:45 - 11:30
5 урок: 11:40 - 12:25
6 урок: 12:35 - 13:20
7 урок: 13:30 - 14:15
8 урок: 14:25 - 15:10
9 урок: 15:20 - 16:05
10 урок: 16:15 - 17:00
11 урок: 17:10 - 18:55"""
    await message.answer(tt)


@dp.message_handler(text="Місцезнаходження ліцею та ін.", state=Steps.workState)
async def bot_place(message: types.Message):
    await message.answer("Місцезнаходження чого саме ви хочете знайти?", reply_markup=place)


@dp.callback_query_handler(text="lyceum", state=Steps.workState)
async def bot_place_lyceum(callback: types.callback_query):
    await bot.send_message(callback.from_user.id, "Геопозиція ліцею:")
    await bot.send_location(callback.from_user.id, 49.228910337047765, 28.40664549489518)


@dp.callback_query_handler(text="canteen", state=Steps.workState)
async def bot_place_canteen(callback: types.callback_query):
    await bot.send_message(callback.from_user.id, "Геопозиція їдальні:")
    await bot.send_location(callback.from_user.id, 49.23256299969235, 28.409144544396877)


@dp.callback_query_handler(text="pe", state=Steps.workState)
async def bot_place_pe(callback: types.callback_query):
    await bot.send_message(callback.from_user.id, "Геопозиція стадіону:")
    await bot.send_location(callback.from_user.id, 49.231997443772315, 28.411318807717414)


@dp.message_handler(text="Розклад уроків", state=Steps.workState)
async def bot_timetable(message: types.Message):
    pull.clear()
    await message.answer("Для яких класів ви хочете отримати розклад?", reply_markup=subjects1)


@dp.callback_query_handler(text="8-9", state=Steps.workState)
async def bot_place_class(callback: types.callback_query):
    pull.update({"class": "8-9"})
    await bot.send_message(callback.from_user.id, "Який день вам потрібен?", reply_markup=subjects2)


@dp.callback_query_handler(text="10-11", state=Steps.workState)
async def bot_place_class(callback: types.callback_query):
    pull.update({"class": "10-11"})
    await bot.send_message(callback.from_user.id, "Який день вам потрібен?", reply_markup=subjects2)


@dp.callback_query_handler(state=Steps.workState)
async def bot_place_class(callback: types.callback_query):
    pull.update({"day": f"{callback.data}"})
    list = await db.select_table_timetable(pull)
    photo = open(f'data\materials\{list[0]["path"]}.jpg', 'rb')
    await bot.send_photo(callback.from_user.id, photo)


@dp.message_handler(text="План ліцею", state=Steps.workState)
async def bot_main(message: types.Message):
    await bot.send_message(message.from_user.id, "Секунду...")
    photo = open('data\materials\plan.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo)
