from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

home = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="Button 1"
            )
        ]
    ],
    resize_keyboard=True
)