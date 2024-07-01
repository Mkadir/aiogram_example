from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette_admin.contrib.sqla import Admin, ModelView
from fastapi import FastAPI, Request
from data.config import SECRET_KEY
from sqlalchemy_file.storage import StorageManager
from libcloud.storage.drivers.local import LocalStorageDriver
import os
from loader import engine
from database.models import Base, Users
from views.auth import UsernameAndPasswordProvider
from views.mvt import UserAdmin


templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="Admin Api",
    description="bot",
    version="0.0.1",
    # docs_url=None,
    # redoc_url=None,
    # openapi_url=None,
    debug=False
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home_page.html", {"request": request})


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)
    os.makedirs("./upload_dir/attachment", 0o777, exist_ok=True)
    container = LocalStorageDriver("./upload_dir").get_container("attachment")
    StorageManager.add_storage("default", container)


app.mount("/images", StaticFiles(directory="images"), name='images')

admin = Admin(engine, base_url='/not-admin', title="Dashboard",
              middlewares=[Middleware(SessionMiddleware, secret_key=SECRET_KEY)],
              auth_provider=UsernameAndPasswordProvider())

admin.add_view(UserAdmin(Users, icon="fa fa-users"))
admin.mount_to(app)
