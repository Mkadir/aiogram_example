from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from database.user_methods import add_user
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    new_user = add_user(
        db=db, data={
            'tg_id':message.from_user.id,
            'name': message.from_user.full_name
        }
    )
    