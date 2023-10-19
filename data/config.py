from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

SQL_DATABASE_URL = "sqlite:///./sql_app.db"

BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
SECRET_KEY = env.str('SECRET_KEY')

CHANNELS = []


