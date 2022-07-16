from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

place = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ліцей", callback_data="lyceum"),

        ],
        [
            InlineKeyboardButton(text="Їдальня", callback_data="canteen")
        ],
        [
            InlineKeyboardButton(text="Стадіон", callback_data="pe")
        ]
    ]
)

subjects1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="8-9 класи", callback_data="8-9"),

        ],
        [
            InlineKeyboardButton(text="10-11 класи", callback_data="10-11")
        ]
    ]
)
subjects2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Понеділок", callback_data="monday")
        ],
        [
            InlineKeyboardButton(text="Вівторок", callback_data="tuesday")
        ],
        [
            InlineKeyboardButton(text="Середа", callback_data="wednesday")
        ],
        [
            InlineKeyboardButton(text="Четвер", callback_data="thursday")
        ],
        [
            InlineKeyboardButton(text="П`ятниця", callback_data="friday")
        ]
    ]
)
