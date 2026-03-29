import os
from dotenv import load_dotenv


# Загружаем переменные окружения из .env файла
load_dotenv()


# Токен бота от @BotFather (рекомендуется хранить в .env)
BOT_TOKEN = os.getenv('BOT_TOKEN')


# URL API для курсов валют
CURRENCY_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
