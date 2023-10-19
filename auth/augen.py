from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.auth import AdminUser, AuthProvider
from starlette_admin.exceptions import FormValidationError, LoginFailed

users = {
    "general": {
        "name": "Muhammadali",
        "avatar": "admin.png",
        "roles": ["read", "create", "edit", "delete", "action_make_published"],
    },
    "bigbro": {
        "name": "Big Bro",
        "avatar": None, # user avatar is optional
        "roles": ["read", "create", "edit", "action_make_published"],
    },
    "botadmins": {
        "name": "Bot Admins",
        "avatar": None, # user avatar is optional
        "roles": ["read", "create", "edit", "action_make_published"],
    }
}


class UsernameAndPasswordProvider(AuthProvider):
    """
    This is only for demo purpose, it's not a better
    way to save and validate user credentials
    """
    passwords = {
        "general": "working1!Q",
        "bigbro": "karshisecurity1!Q",
        "botadmins": "bot123"
    }

    async def login(
        self,
        username: str,
        password: str,
        remember_me: bool,
        request: Request,
        response: Response,
    ) -> Response:
        if len(username) < 3:
            """Form data validation"""
            raise FormValidationError(
                {"username": "Ensure username has at least 03 characters"}
            )

        if username in users and password == self.passwords.get(username):
            """Save `username` in session"""
            request.session.update({"username": username})
            return response

        raise LoginFailed("Invalid username or password")

    async def is_authenticated(self, request) -> bool:
        if request.session.get("username", None) in users:
            """
            Save current `user` object in the request state. Can be used later
            to restrict access to connected user.
            """
            request.state.user = users.get(request.session["username"])
            return True

        return False

    def get_admin_user(self, request: Request) -> AdminUser:
        user = request.state.user  # Retrieve current user
        photo_url = None
        if user["avatar"] is not None:
            pass
            # photo_url = request.url_for("static", path=user["avatar"])
        return AdminUser(username=user["name"],
                         photo_url='https://img.freepik.com/free-vector/businessman-character-avatar-isolated_24877'
                                   '-60111.jpg?w=740&t=st=1692193263~exp=1692193863~hmac'
                                   '=8d3de9364af0dccc51bf5b8a9988ee293332881bc6ef058e362f94440d0f0eef'
                         )

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response