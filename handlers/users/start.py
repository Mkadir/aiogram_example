from loader import bot, db, dp
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(state="*", commands=['start'])
async def start_command(message: types.Message, state: FSMContext):
    await message.answer(
        text=f"Salom {message.from_user.full_name}"
    )

