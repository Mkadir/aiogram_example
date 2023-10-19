from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.simple import admin_panel_keys
from loader import dp
from utils.extra import get_admin_conf

ADMINS = get_admin_conf()


@dp.message_handler(user_id=ADMINS, commands=['admin'], state="*")
async def admin_panel(message: types.Message, state: FSMContext):
    text = """
<b>🆗 Admin panelga xush kelibsiz</b>
    """
    await message.answer(text, reply_markup=admin_panel_keys, disable_web_page_preview=True)
    await state.finish()


