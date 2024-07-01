from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppData, WebAppInfo

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
