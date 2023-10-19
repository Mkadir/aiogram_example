from models.btm import BotAdmin
from sqlalchemy.orm import Session


def get_admins(db: Session):
    return db.query(BotAdmin).all()
