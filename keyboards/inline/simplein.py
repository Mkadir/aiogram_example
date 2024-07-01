from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Button 1",
                callback_data="button 1 clicked"
            )
        ]
    ]
)

