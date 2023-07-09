from sqlalchemy import Column, Integer, String, Boolean
from loader import Base

class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    tg_id = Column(Integer, unique=True)
    name = Column(String)

    def __str__(self):
        return self.name