import asyncio

from aiogram.dispatcher import FSMContext

from database.methods import get_users
from keyboards.default.simple import admin_panel_keys
from keyboards.inline.simplein import admin_cancel, admin_yes_no
from loader import dp, bot, db
from aiogram import types

from utils.extra import get_admin_conf

ADMINS = get_admin_conf()


@dp.message_handler(user_id=ADMINS, text="📩 Xabar yuborish")
async def admin_send_message(message: types.Message, state: FSMContext):
    test_message = await message.answer("...", reply_markup=types.ReplyKeyboardRemove())
    await test_message.delete()
    await state.finish()
    text = """
<b>
Quyidagi xabar turidan birini yuboring:
● Text
● Rasm
● Video
● Audio
</b>
    """
    await message.answer(
        text=text,
        reply_markup=admin_cancel
    )
    await state.set_state("wait_for_send_type")


@dp.callback_query_handler(user_id=ADMINS, text="admin_cancel", state="*")
async def admin_cancel_send(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.answer(
        text="<b>Amaliyot bekor qilindi</b>",
        reply_markup=admin_panel_keys
    )
    await state.finish()


@dp.message_handler(user_id=ADMINS, content_types=['any'], state="wait_for_send_type")
async def admin_send_message(message: types.Message, state: FSMContext):
    # await message.edit_reply_markup()
    # await state.finish()
    # print(message.content_type)
    if message.content_type == "text":
        text = message.text
        await message.answer(text=text)
        await message.answer(
            text="<b>Xabar shu tarzda yuboriladi, tasdiqlaysizmi ?</b>", reply_markup=admin_yes_no)
        await state.set_state("wait_for_confirm")
        await state.update_data(text=text, ads_type="text")
    elif message.content_type == "photo":
        file_id = message.photo[-1].file_id
        caption = message.caption
        await message.answer_photo(
            photo=file_id,
            caption=caption
        )
        await message.answer(
            text="<b>Xabar shu tarzda yuboriladi, tasdiqlaysizmi ?</b>", reply_markup=admin_yes_no)
        await state.set_state("wait_for_confirm")
        await state.update_data(file_id=file_id, caption=caption, ads_type="photo")
    elif message.content_type == "video":
        file_id = message.video.file_id
        caption = message.caption
        await message.answer_video(
            video=file_id,
            caption=caption
        )
        await message.answer(
            text="<b>Xabar shu tarzda yuboriladi, tasdiqlaysizmi ?</b>", reply_markup=admin_yes_no)
        await state.set_state("wait_for_confirm")
        await state.update_data(file_id=file_id, caption=caption, ads_type="video")
    elif message.content_type == "audio":
        file_id = message.audio.file_id
        caption = message.caption
        await message.answer_audio(
            audio=file_id,
            caption=caption,

        )
        await message.answer(
            text="<b>Xabar shu tarzda yuboriladi, tasdiqlaysizmi ?</b>", reply_markup=admin_yes_no)
        await state.set_state("wait_for_confirm")
        await state.update_data(file_id=file_id, caption=caption, ads_type="audio")
    else:
        await message.answer(
            text="<b>Xabar turi noto'g'ri kiritlgan ko'rinadi, qaytadan urinib ko'ring</b>",
            reply_markup=admin_cancel
        )
        await state.set_state("wait_for_send_type")


@dp.callback_query_handler(user_id=ADMINS, text="admin_yes", state="wait_for_confirm")
async def admin_confirm_message(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    data = await state.get_data()
    users = get_users(db)
    iterable = users
    length = 10
    total = None
    if total is None:
        try:
            total = len(iterable)
        except TypeError:
            raise TypeError("Error")
    ads_type = data.get("ads_type")
    await call.message.answer(
        text="<b>Xabar yuborish boshlandi, yakunlangach xabar beraman</b>",
    )
    msg = await call.message.answer(text="....")
    await state.finish()
    sent = 0
    if ads_type == "text":
        text = data.get("text")
        for i, user in enumerate(users):
            if i > 0 and i % 20 == 0:
                await asyncio.sleep(1)
            progress = int(length * (i + 1) / total)
            bar = "[" + "▪️" * progress + "◻️" * (length - progress) + "]"
            message_to_sent = f"\r{bar} {i + 1}/{total}"
            try:
                await bot.send_message(user, text=text)
                sent += 1
            except Exception as e:
                print(e)
            try:
                await msg.edit_text(
                    message_to_sent
                )
            except Exception as e:
                print(e)
    elif ads_type == "photo":
        file_id = data.get("file_id")
        caption = data.get("caption")
        for i, user in enumerate(users):
            if i > 0 and i % 20 == 0:
                await asyncio.sleep(1)
            progress = int(length * (i + 1) / total)
            bar = "[" + "▪️" * progress + "◻️" * (length - progress) + "]"
            message_to_sent = f"\r{bar} {i + 1}/{total}"
            try:
                await bot.send_photo(
                    chat_id=user,
                    photo=file_id,
                    caption=caption
                )
                sent += 1
            except Exception as e:
                print(e)

            try:
                await msg.edit_text(
                    message_to_sent
                )
            except Exception as e:
                print(e)
    elif ads_type == "video":
        file_id = data.get("file_id")
        caption = data.get("caption")
        for i, user in enumerate(users):
            if i > 0 and i % 20 == 0:
                await asyncio.sleep(1)
            progress = int(length * (i + 1) / total)
            bar = "[" + "▪️" * progress + "◻️" * (length - progress) + "]"
            message_to_sent = f"\r{bar} {i + 1}/{total}"
            try:
                await bot.send_video(
                    chat_id=user,
                    video=file_id,
                    caption=caption
                )
                sent += 1
            except Exception as e:
                print(e)

            try:
                await msg.edit_text(
                    message_to_sent
                )
            except Exception as e:
                print(e)
    elif ads_type == "audio":
        file_id = data.get("file_id")
        caption = data.get("caption")
        for i, user in enumerate(users):
            if i > 0 and i % 20 == 0:
                await asyncio.sleep(1)
            progress = int(length * (i + 1) / total)
            bar = "[" + "▪️" * progress + "◻️" * (length - progress) + "]"
            message_to_sent = f"\r{bar} {i + 1}/{total}"
            try:
                await bot.send_audio(
                    chat_id=user,
                    audio=file_id,
                    caption=caption
                )
                sent += 1
            except Exception as e:
                print(e)

            try:
                await msg.edit_text(
                    message_to_sent
                )
            except Exception as e:
                print(e)
    await call.message.answer(
        text=f"Xabaringiz {sent} ta foydalanuvchiga yuborildi."
    )


@dp.callback_query_handler(user_id=ADMINS, text="admin_no", state="wait_for_confirm")
async def admin_confirm_message(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await state.finish()
    await call.message.answer(
        text="Admin panel",
        reply_markup=admin_panel_keys
    )