from datetime import datetime

from database.db import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime


class BotAdmin(Base):
    __tablename__ = "Admin"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    name = Column(String)

    def __str__(self):
        return self.name


