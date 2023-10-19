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

admin_cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⭕️ Bekor qilish",
                callback_data="admin_cancel"
            )
        ]
    ]
)

admin_yes_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Ha",
                callback_data="admin_yes"
            ),
            InlineKeyboardButton(
                text="❌ Yo'q",
                callback_data="admin_no"
            )
        ]
    ]
)

channels_vs_join = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 Kanallar",
                url="https://t.me/addlist/4Q5-1ov24qAxMTQy"
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ A'zo bo'ldim",
                callback_data='joined_channels'
            )
        ]
    ]
)


def create_share_btn(link: str, user):
    share_text = f"""
💰 SOQQALI KONKURSGA start berdildi!!!

{user} doʻstingiz sizni konkursga taklif qilmoqda. 

Har bir ovoz uchun 1000 so'm, to'lovlar avto ✅

👇🏻 Konkursda ishtirok etish uchun bosing:"""
    text = f"{link}"

    share_link = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Taklif qilish",
                                     url=f"https://t.me/share/url?text={text}&url={share_text}")
            ]
        ],
    )
    return share_link


multi_card_login = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔓 Login-MultiCard",
                callback_data='login_multi_card'
            )
        ]
    ]
)

multi_card_home = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔓 Hisobni o'zgartirish",
                callback_data='login_multi_card'
            ),
            InlineKeyboardButton(
                text="⭕️ Bekor qilish",
                callback_data="admin_cancel"
            )
        ]
    ]
)

cancel_user = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⭕️ Bekor qilish",
                callback_data="user_cancel"
            )
        ]
    ]
)

withdraw = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📤 Yechib olish",
                callback_data="withdraw_user_money"
            )
        ],
        [
            InlineKeyboardButton(
                text="⭕️ Bekor qilish",
                callback_data="user_cancel"
            )
        ]
    ]
)


def payment_key_generator(card_id: str, amount: int, payment_id:int):

    approve_payment = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Tasdiqlash",
                    callback_data=f'pay_{payment_id}_{card_id}_{amount}'
                )
            ]
        ]
    )
    return approve_payment