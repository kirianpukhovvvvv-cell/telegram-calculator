import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_API_TOKEN не найден в переменных окружения")
