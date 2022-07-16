from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

request_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Надіслати контакт", request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Головна")
        ],
        [
            KeyboardButton(text="Розклад уроків"),
            KeyboardButton(text="Розклад дзвінків")
        ],
        [
            KeyboardButton(text="Місцезнаходження ліцею та ін.")
        ],
        [
            KeyboardButton(text="План ліцею")
        ]
    ],
    resize_keyboard=True
)
