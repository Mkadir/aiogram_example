from typing import Dict, Any

from starlette.requests import Request
from starlette_admin.exceptions import FormValidationError

from database.models import Users
from starlette_admin.contrib.sqla import ModelView

from loader import Session, db


class UserAdmin(ModelView):
    model = Users
    name = "Users"
    label = "Users"
    icon = "fa fa-users"

    sortable_field = ["id", "tg_user_id", "username"]

    sortable_field_mapping = {
        "id": Users.id,
        "tg_user_id": Users.tg_id,
        "username": Users.username
    }