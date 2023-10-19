import asyncio
import binascii

from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.deep_linking import decode_payload
from aiogram.utils.exceptions import Throttled

from data.config import CHANNELS
from database.methods import get_user, add_user_in_middlewares, update_last_join
from keyboards.inline.simplein import channels_vs_join
from loader import bot, db


class JoinHelper(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user_id = update.message.from_user.id
            user = get_user(db=db, telegram_id=user_id)
            if user:
                pass  # That means ignore if user exists
                # print(user)
            else:
                args = update.message.get_args()
                invited = 0
                if args:
                    try:
                        payload = decode_payload(args)
                        if payload.isdigit():
                            if int(payload) != user_id:
                                invited = payload
                                # invited = payload
                        else:
                            pass  # That means payload None
                    except binascii.Error:
                        pass  # That means payload None
                add_user_in_middlewares(db=db, telegram_id=user_id, invited_user=invited,
                                        full_name=update.message.from_user.full_name,
                                        username=update.message.from_user.username)
            if not (await self.check_user_subs(user_id=user_id)):
                if user.is_verified:
                    update_last_join(db=db, telegram_id=user_id)

                try:
                    await update.message.answer(
                        text="Konkursda ishtirok etish uchun barcha kanallarga a'zo  bo'ling!",
                        reply_markup=channels_vs_join
                    )
                except Exception as e:
                    ...
                raise CancelHandler()

        if update.callback_query:
            user_id = update.callback_query.from_user.id
            if not (await self.check_user_subs(user_id=user_id)):
                await update.callback_query.answer(
                    text="Siz barcha kanallarga a'zo bo'lmadingiz !",
                    show_alert=True
                )
                raise CancelHandler()

    async def check_user_subs(self, user_id):
        status = True
        for i in CHANNELS:
            is_member = await bot.get_chat_member(chat_id=i, user_id=user_id)
            if not is_member.is_chat_member():
                status *= False

        return status
