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

admin_panel_keys = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text="📊 Statistika"
            ),
            KeyboardButton(
                text="📩 Xabar yuborish"
            )
        ]
    ]
)

phone_share = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text="✅ Ro'yhatdan o'tish",
                request_contact=True
            )
        ]
    ]
)