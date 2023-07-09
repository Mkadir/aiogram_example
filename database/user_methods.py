from sqlalchemy.orm import Session
from .models import Users


def add_user(db: Session, data: dict):
    """
    data = {
    'tg_id': 12152,
    'name': 'John uik'
    }
    """

    try:
        new_user = Users(
        tg_id=data['tg_id'],
        name=data['name']
    )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        ...
        # here some exceptions 
    finally:
        db.close()
    return new_user