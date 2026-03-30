import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_API_TOKEN')
CREATOR_ID = 5033224854
# Секретная команда для переключения режима
SECRET_COMMAND = "/secretmode"
