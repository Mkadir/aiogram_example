from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

SQL_DATABASE_URL = "sqlite:///./sql_app.db"

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
SECRET_KEY = env.str('SECRET_KEY')
WEB_ADMINS = env.list("WEB_ADMINS")
WEB_PASSWORD = env.list("WEB_PASSWORD")
quran_icon = 'https://cdn-icons-png.flaticon.com/512/6565/6565365.png'
auth_users = dict(map(lambda x: (x[0], x[1]), zip(WEB_ADMINS, WEB_PASSWORD)))
CHANNELS = []


