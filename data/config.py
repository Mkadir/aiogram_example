from environs import Env


env = Env()
env.read_env()

SQL_DATABASE_URL = "sqlite:///./sql_app.db"

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
SECRET_KEY = env.str('SECRET_KEY')
WEB_ADMINS = env.list("WEB_ADMINS")
WEB_PASSWORD = env.list("WEB_PASSWORD")
auth_users = dict(map(lambda x: (x[0], x[1]), zip(WEB_ADMINS, WEB_PASSWORD)))
CHANNELS = []


