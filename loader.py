from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

engine = create_engine(config.SQL_DATABASE_URL, connect_args={
    'check_same_thread': False
})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

db = Session()
bot['db'] = db
