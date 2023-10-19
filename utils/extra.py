from loader import db
from database.methods import get_admins


def get_admin_conf():
    admins = get_admins(db)
    admins = [admin.telegram_id for admin in admins]
    return admins



