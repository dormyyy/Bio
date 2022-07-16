from aiogram.dispatcher.filters.state import StatesGroup, State


class Steps(StatesGroup):
    startState = State()
    nameState = State()
    phoneState = State()
    preworkState = State()
    workState = State()
