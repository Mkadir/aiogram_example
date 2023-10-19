from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .joining import JoinHelper


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    # dp.middleware.setup(JoinHelper())