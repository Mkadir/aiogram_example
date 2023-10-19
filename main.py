from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette_admin.contrib.sqla import Admin, ModelView
from fastapi import FastAPI, Request
from data.config import SECRET_KEY

from auth.augen import UsernameAndPasswordProvider
from loader import engine

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="Example",
    description="bot",
    version="0.0.1",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
    debug=False
)

# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     return templates.TemplateResponse("homepage.html", {"request": request})


app.mount("/images", StaticFiles(directory="images"), name='images')

admin = Admin(engine, base_url='/not-admin', title="Sam Dashboard", auth_provider=UsernameAndPasswordProvider(),
              middlewares=[Middleware(SessionMiddleware, secret_key=SECRET_KEY)])


class BotUserAdmin(ModelView):
    pass


admin.mount_to(app)
